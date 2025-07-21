import streamlit as st
from collections import deque
graph = {
    "Pune": ["Mumbai", "Satara", "Nashik"],
    "Mumbai": ["Pune", "Nashik", "Ahmedabad"],
    "Satara": ["Pune", "Kolhapur", "Sangli"],
    "Kolhapur": ["Satara", "Belgaum"],
    "Belgaum": ["Kolhapur", "Hubli"],
    "Hubli": ["Belgaum", "Bangalore"],
    "Nashik": ["Pune", "Mumbai", "Aurangabad"],
    "Aurangabad": ["Nashik", "Nagpur", "Solapur"],
    "Solapur": ["Aurangabad", "Hyderabad"],
    "Hyderabad": ["Solapur", "Bangalore"],
    "Bangalore": ["Hyderabad", "Hubli", "Chennai"],
    "Chennai": ["Bangalore"],
    "Sangli": ["Satara", "Miraj"],
    "Miraj": ["Sangli", "Ichalkaranji"],
    "Ichalkaranji": ["Miraj", "Kolhapur"],
    "Ahmedabad": ["Mumbai", "Surat"],
    "Surat": ["Ahmedabad", "Vadodara"],
    "Vadodara": ["Surat", "Indore"],
    "Indore": ["Vadodara", "Nagpur"],
    "Nagpur": ["Indore", "Aurangabad"]
}
def bfs(graph,start,goal):
    visited = set()
    queue = deque([[start]])
    if start == goal:
        return [start]
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            neighbours = graph.get(node, [])
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            visited.add(node)
    return None
st.title("🧭 GPS Navigation using BFS")
st.write("Enter two locations to find the shortest route between them:")
start = st.selectbox("Start Location", list(graph.keys()))
end = st.selectbox("Destination", list(graph.keys()))
if st.button("Find Route"):
    route = bfs(graph, start, end)
    if route:
        st.success("➡️ Shortest route: " + " → ".join(route))
    else:
        st.error("No route found between the selected cities.")