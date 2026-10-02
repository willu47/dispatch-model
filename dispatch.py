import  pypsa

n = pypsa.Network()
n.snapshots = [1, 2, 3]

n.add("Bus", "gen_bus", carrier="transmission")
n.add("Bus", "load_bus")
n.add("Load", "load_1", bus="load_bus", p_set=[324, 253, 335])
n.add(
    "Link",
    "transmission",
    bus0="gen_bus",
    bus1="load_bus",
    efficiency=0.93,
    p_nom=1000,
)

n.add("Generator",
      "coal",
      bus="gen_bus",
      p_nom=700,
      marginal_cost=4,
)

n.optimize()
print(n.generators_t.p)
n.model.to_file("dispatch.lp")

