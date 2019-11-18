import statistics
xyz=[21600,4350,3920,5590,3250,4010]
srednia=statistics.mean(xyz)
mediana=statistics.median(xyz)
odchylenie=statistics.pstdev(xyz)
print(f"a. średnia arytmetyczna wynagrodzeń wynosi {srednia}")
print(f"b. mediana wynagrodzeń wynosi {mediana}")
print(f"c. odchylenie standartowe wynagrodzeń wynosi {odchylenie}")
