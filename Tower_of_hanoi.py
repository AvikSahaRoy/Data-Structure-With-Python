def tower_of_hanoi(disks, source, destination, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
    else:
        tower_of_hanoi(disks - 1, source, target, destination)  
        print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
        tower_of_hanoi(disks - 1, destination, source, target)  
  
disks = int(input('Enter the number of disks: '))  
tower_of_hanoi(disks, 'A', 'B', 'C')