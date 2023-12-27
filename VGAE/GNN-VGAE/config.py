import torch

dvc = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
chemical_elements = ["C", "N", "O", "F", "P", "S", "Cl", "Br", "I"]
atomic_nr = [6, 7, 8, 9, 15, 16, 17, 35, 53]
edges = ["1", "2", "3", "M"]
max_molecule_size = 20
