<img src="https://github.com/inaki-ortizdelandaluce/spooky/blob/main/icons/spookey-afterglow-full-jelly.png?raw=true"/>

# Spookey: A satellite QKD modelling and simulation software

## Introduction
Spookey is a software toolkit for satellite-based QKD (SatQKD) mission analysis. 
It supports modelling of various SatQKD hardware components, such as photon sources, detectors, and telescopes, 
and its configuration within a network of satellites and optical ground stations. Spookey offers 
capabilities to simulate several discrete-variable QKD protocols considering different geographical, orbital, 
and atmospheric conditions. Figures of merit such as satellite link budget and secure key rate can be computed to 
evaluate the feasibility of a given mission profile and its viability with respect to use cases with specific 
requirements regarding key latency and generation rates.

Spookey relies on standard open-source tools and libraries to ensure unrestricted further development and seamless 
integration within a broader spectrum of mission planning tools.
 
Currently, no such comprehensive software exists in the market that allows for detailed analysis of SatQKD missions in 
a fully integrated fashion. The final goal of this toolkit is to equip future SatQKD operators with advanced modelling, 
simulation, and feasibility analysis competences. By providing detailed insights into hardware configurations, 
protocol capabilities, and environmental impacts, this tool will enable end-users seeking for unconditional security, 
to comprehensively evaluate the viability of their business cases, thus paving the way for informed decision-making 
and strategic planning in the rapidly evolving field of quantum cryptography and communication.

## Poetry quick guide (see https://python-poetry.org/docs/cli/)
````
poetry new --src --name my.package my-package
poetry init
poetry install
poetry update
poetry add package
poetry add package@^X.Y.Z
poetry add "package>=X.Y.Z"
poetry add package@latest
poetry remove package
poetry shell
poetry show --tree
````
