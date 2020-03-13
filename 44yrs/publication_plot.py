from pathlib import Path
import pandas as pd
from math import floor
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (5.0, 2.3)
plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = (
    "\\usepackage{mathpazo}" + "\n" + "\\usepackage{siunitx}"
)


def format_year_to_datetime(data: pd.Series):
    new_date = []
    for d in data:
        year = floor(d)
        days = (d - year) * 365

        new_date.append(datetime(year, 1, 1) + timedelta(days=days))

    return pd.DataFrame(new_date)


fig, ax = plt.subplots()

for name, cname, color, label in [
    ("watts", "watts", "C4", "Typical Power $\\left[ \\si{\\watt} \\right]$"),
    (
        "frequency",
        "frequency",
        "C1",
        "Frequency $\\left[ \\si{\\mega\\hertz} \\right]$",
    ),
    (
        "specint",
        "specint",
        "C2",
        "Single-Thread Perf. \n $\\left[\\text{SpecINT}\\times\\num{e3}\\right]$",
    ),
    ("cores", "n_cores", "C0", "Logical Cores"),
    (
        "transistors",
        "transistors",
        "C3",
        "Transistors $\\left[ \\num{e3} \\right]$",
    ),
]:
    df = pd.read_csv(Path(__file__).parent / f"{name}.csv")
    df = df.rename(columns={f" {cname}": f"{name}"})
    df["year"] = format_year_to_datetime(df["year"])
    ax.plot(df["year"], df[name], "o", color=color, label=label, markersize=3)

ax.set_title("Microprocessor Trend Data")
ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5), labelspacing=1.0)
ax.grid(axis="y", which="major", linestyle="dashed")

ax.set_xlabel("year")
ax.set_xlim(datetime(1970, 1, 1), datetime(2020, 1, 1))
x_years = np.arange(1970, 2030, 10)
ax.set_xticks([datetime(y, 1, 1) for y in x_years])
ax.set_xticklabels([y for y in x_years])

ax.set_yscale("log")
ax.set_ylim(0.2, 5e8)
ax.set_yticks(np.logspace(0, 8, 5))
ax.set_ylabel("")
plt.tight_layout(pad=0.2)
fig.savefig("44-years-processor-trend.pdf")
