from invoke import task

@task(default=True)
def package(c, n="switch-dip"):
    c.run("rm -rf order/*", warn=True)
    c.run(f"cp out/{n}-F_Cu.gbr order/{n}.GTL")
    c.run(f"cp out/{n}-B_Cu.gbr order/{n}.GBL")
    c.run(f"cp out/{n}-F_Mask.gbr order/{n}.GTS")
    c.run(f"cp out/{n}-B_Mask.gbr order/{n}.GBS")
    c.run(f"cp out/{n}-F_SilkS.gbr order/{n}.GTO")
    c.run(f"cp out/{n}-B_SilkS.gbr order/{n}.GBO")
    c.run(f"cp out/{n}-PTH.drl order/{n}.TXT")
    c.run(f"cp out/{n}-NPTH.drl order/{n}-NPTH.TXT")
    c.run(f"cp out/{n}-Edge_Cuts.gbr order/{n}.GML")
    with c.cd("order"):
        c.run(f"zip _.zip {n}*")
        c.run(f"mv _.zip {n}.zip")
