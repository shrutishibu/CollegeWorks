#tower of hanoi
def TowerOfHanoi(n, source, auxilary, target):
  if n==1:
    print(f"Move disk 1 from {source} to {target}")
    return
  TowerOfHanoi(n-1, source, target, auxilary)
  print(f"Moved disk {n} from {source} to {target}")
  TowerOfHanoi(n-1, auxilary, source, target)
n = int(input("Enter disks: "))
TowerOfHanoi(n, 'A', 'B', 'C')