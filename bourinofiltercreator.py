"""
Program written by Arnold Dechamps
Was written because I was to leasy to manually write in/out filter-lists to
apply to about 100 peers.
"""

def peerrecorder(names):
    """
    Only taking peer names to create all the rules
    """
    print("""Write "Telerys" to end""")
    while True:
        names.append(str(input("Peer Name : ")))
        if names[len(names)-1] == "Tiguinet":
            break

def localprefwritter():
    """
    Taking local-pref from user... (used for transit/peering distinction)
    returns the local-pref value
    """
    return str(input("What is the local-pref to set : "))

def listgenerator(names, localpref):
    """
    Function outputs lines to put in the role for the CLI
    """
    for i in range(len(names)-1):
        print('/routing filter add chain='+names[i]+'-in invert-match=no action=jump jump-target=self-net-in set-bgp-prepend-path=""')
        print('/routing filter add chain='+names[i]+'-in invert-match=no action=accept set-bgp-local-pref='+localpref+' set-bgp-prepend-path=""')
        print('/routing filter add chain='+names[i]+'-out invert-match=no action=jump jump-target=self-net-out set-bgp-prepend-path=""')
        print('/routing filter add chain='+names[i]+'-out invert-match=no action=discard set-bgp-prepend-path=""')

def main():
    """
    Main loop
    """
    while True:
        peername = []
        peerrecorder(peername)
        listgenerator(peername,localprefwritter())
        if str(input("Press q to quit ")) == "q":
            break

# To be able to execute program while not launching in if importing
if __name__ == '__main__':
    main()
