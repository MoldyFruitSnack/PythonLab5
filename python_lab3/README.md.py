
    #function name
    #parameters
    #returns anything?
# Example 
def chat_task(ctx, pipe, n, group):  # function name is chat_task
    ctx: This is a ZeroMQ Connection Context
    pipe: This is a communications pipe polled by ZeroMQ for messages.
    n: This is the peer to peer node my chat app is connected as
    group: This is the peer chat group I wanted to join
#The chat_task method does not return anything, it appears to be the send/recieve manager.

def get_peer_node(username):   # function name is get_peer_node
    username # This is your username that you will receive from the get_username function
# This function returns something that looks like a pyre node?
def join_group(node, group):   # function name is join_group
    node # I assume this is my peer computer node
    group # I assume this is a group I want to join from the get_group function
# This function does not return anything 

def get_channel(node, group):   # function name is get_channel
    node # I assume this is my peer computer node
    group # I assume this is a group I want to join from the get_group function
# This function returns a zhelper. not to sure but it could be a channel from a node or group. 



