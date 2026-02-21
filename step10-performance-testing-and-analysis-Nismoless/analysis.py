from irsystem import InformationRetrievalSystem
from irshashdict import IRSystemHashDict
from irsbstdict import IRSystemBST
from irsystemsldict import IRSystemSL
from irslldict import IRSystemLL
import time # importing the time to calcuate the time needed to run the queries
import random # generating random numbers


def song_inventory_analysis(rand_file_name, no_queries, no_entries):
    # list based inventory
    inventory = InformationRetrievalSystem()
    inventory.load_data(rand_file_name)
    # bst dict based inventory
    inventory_bst = IRSystemBST()
    inventory_bst.load_data(rand_file_name)
    # ll dict based inventory
    inventory_ll = IRSystemLL()
    inventory_ll.load_data(rand_file_name)
    # sl dict based inventory
    inventory_sl = IRSystemSL()
    inventory_sl.load_data(rand_file_name)
    # hash table based inventory
    inventory_ht = IRSystemHashDict()
    inventory_ht.load_data(rand_file_name)

    # generate random song_ids to query
    random_songid_list = []
    for i in range(0, no_queries):
        n = random.randint(1, no_entries)
        random_songid_list.append(n)

    # LIST BASED IMPLEMENTATION ################################################################
    # start timer
    start_time = time.time()
    results1 = []
    # run queries
    for rand_id in random_songid_list:
        result = inventory.search_by_id(rand_id)
        results1.append(result)
    # calc/output total time to search 
    end_time = time.time()
    print("No of entries: " + str(no_queries))
    list_time = end_time - start_time
    print("searching " + str(no_queries) + " queries using the list based implementation: ---%s seconds ---" %(list_time))
    #############################################################################################
    # BST BASED IMPLEMENTATION ##################################################################
    # start timer
    start_time = time.time()
    results1 = []
    # run queries
    for rand_id in random_songid_list:
        result = inventory_bst.search_by_id(rand_id)
        results1.append(result)
    # calc/output total time to search 
    end_time = time.time()
    print("No of entries: " + str(no_entries))
    bst_time = end_time - start_time
    print("searching " + str(no_queries) + " queries using the bst based implementation: ---%s seconds ---" %(bst_time))
    #############################################################################################
    # LL BASED IMPLEMENTATION ##################################################################
    # start timer
    start_time = time.time()
    results1 = []
    # run queries
    for rand_id in random_songid_list:
        result = inventory_ll.search_by_id(rand_id)
        results1.append(result)
    # calc/output total time to search 
    end_time = time.time()
    print("No of entries: " + str(no_entries))
    ll_time = end_time - start_time
    print("searching " + str(no_queries) + " queries using the linked list based implementation: ---%s seconds ---" %(ll_time))
    #############################################################################################
    # SL BASED IMPLEMENTATION ##################################################################
    
    for rand_id in random_songid_list:
        result = inventory_sl.search_by_id(rand_id)
        results1.append(result)
    # calc/output total time to search 
    end_time = time.time()
    print("No of entries: " + str(no_entries))
    sl_time = end_time - start_time
    print("searching " + str(no_queries) + " queries using the sorted list based implementation: ---%s seconds ---" %(sl_time))
    #############################################################################################
    # HASH TABLE BASED IMPLEMENTATION ##################################################################
    # start timer
    start_time = time.time()
    results1 = []
    # run queries
    for rand_id in random_songid_list:
        result = inventory_ht.search_by_id(rand_id)
        results1.append(result)
    # calc/output total time to search 
    end_time = time.time()
    print("No of entries: " + str(no_entries))
    ht_time = end_time - start_time
    print("searching " + str(no_queries) + " queries using the hash table based implementation: ---%s seconds ---" %(ht_time))
    #############################################################################################

# song_inventory_analysis("datafiles/rand_file_100.csv", 100, 100)