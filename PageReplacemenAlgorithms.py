from queue import Queue

def pageFaults(pages, n, capacity):
	s = set()
	indexes = Queue()
	page_faults = 0
	for i in range(n):
		if (len(s) < capacity):
            if (pages[i] not in s):
				s.add(pages[i])
				page_faults += 1
				indexes.put(pages[i])
		else:
			if (pages[i] not in s):
				val = indexes.queue[0]
				indexes.get()
				s.remove(val)
				s.add(pages[i])
				indexes.put(pages[i])
				page_faults += 1
	return page_faults


#driver code
i = 0
if __name__ == '__main__':
    pages = []
    capacity = int(input("How many frame you want your table to have: "))
    numberOfPage = int(input("Enter you number of page: "))
	while len(pages) < numberOfPage:
         print("your",i,"sequence")
         pagesObject = input("Please enter your pages sequence:" )
         pages.append(pagesObject)
         i += 1
	n = len(pages)
    print("This is the page fault you will get:",pageFaults(pages, n, capacity))
