# Simulate API traffic hitting a microservice

requests_per_second = 120
requests_per_container_capacity = 30

containers_required = requests_per_second / requests_per_container_capacity

cpu_cost_per_container = 45   # monthly cost

monthly_cost = containers_required * cpu_cost_per_container

print("Requests per second:", requests_per_second)
print("Container capacity:", requests_per_container_capacity)
print("Containers required:", containers_required)
print("Monthly infrastructure cost:", monthly_cost)
