import plotly.graph_objects as go
import Node
from Grid import Grid
#Shout out to my boy Abel couldn't have done this Graph without these two classes excited to have done some work that helped -
class Graph:
    def __init__(self, budget=50, radius=5, type=0):
        self.grid = Grid(budget=budget, radius=radius, type=type)
        self.circle_x = 10  # x-coordinate of the center of the circle
        self.circle_y = 10  # y-coordinate of the center of the circle
        self.circle_radius = 5  # radius of the circle
        self.budget = budget
        self.enclosed_cost = 0 
    
    def plot(self):
        # Generate a scatter plot of all nodes in the grid
        x = [node.getX() for node in self.grid.getNodes()]
        y = [node.getY() for node in self.grid.getNodes()]
        cost = [node.getCost() for node in self.grid.getNodes()]
        
        # Create a color map to color code each algorithm
        colors = {'Random Algorithm': 'blue', 'Pure Greedy Algorithm': 'green', 'Greedy Set Cover Algorithm': 'red'}
        
        # Initialize the figure
        fig = go.Figure()
        
        # Add a scatter trace for all nodes in the grid
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='gray'), text=cost, 
                                hovertemplate='(%{x}, %{y})<br>Cost: %{text:.2f}<extra></extra>', name='All Nodes'))
        
        # Add a trace for each algorithm
        for i, (name, nodes) in enumerate([('Random Algorithm', self.grid.randomAlgorithm()), 
                            ('Pure Greedy Algorithm', self.grid.pureGreedyAlgorithm()), 
                            ('Greedy Set Cover Algorithm', self.grid.greedySetCoverAlgorithm())]):
            
            # Draw circles for the nodes selected by the algorithm
            self.draw_circle(fig, nodes, self.budget, color=colors[name])

            
            # Add a legend for the algorithm
            fig.add_trace(go.Scatter(x=[], y=[], mode='markers', marker=dict(color=colors[name]), 
                              name=name, showlegend=True))
        
        # Customize the layout of the scatter plot
        fig.update_layout(title="Node Scatter Plot", xaxis_title="Coverage", yaxis_title="Radius", height=600, width=800, margin=dict(l=50, r=50, b=50, t=50, pad=4),legend=dict(title='Algorithms', yanchor='top', y=1.0, xanchor='left', x=0.1))
                        #xaxis=dict(range=[0,50]), # Controls the range of the x-axis to an extent 
                        #yaxis=dict(range=[0,5]),  # Controls the range of the y-axis to an extent
        
        fig.show()


    def draw_circle(self, fig, nodes: list[Node.Node], budget: int, color: str):
        # calculate the center of the circle
        if not nodes:  # check if nodes is empty
            print("Error: nodes parameter is empty")
            return
        center_x = sum(node.getX() for node in nodes) / len(nodes)
        center_y = sum(node.getY() for node in nodes) / len(nodes)

        # calculate the radius of the circle
        max_distance = max(((node.getX() - center_x) ** 2 + (node.getY() - center_y) ** 2) ** 0.5 for node in nodes)
        self.circle_radius = max_distance * .1
        self.circle_x = center_x
        self.circle_y = center_y

        for node in nodes:
            fig.add_shape(type="circle", xref="x", yref="y", x0=node.getX()-self.circle_radius, y0=node.getY()-self.circle_radius, x1=node.getX()+self.circle_radius, y1=node.getY()+self.circle_radius, line=dict(color=color, width=2, dash='dash')) #Visually encircles nodes
            fig.add_annotation(x=self.circle_x, y=self.circle_y,text=f'Budget: {budget:.2f}<br>Enclosed cost: {self.enclosed_cost:.2f}',font=dict(size=16), showarrow=False, bgcolor = 'white', bordercolor = 'black', borderwidth = 2, borderpad = 4) #Adds the textbox to the graph


                
              

# Creating the example and printing it out
graph = Graph()
#graph.find_nodes_randomly()
graph.plot()
