class MockServerAPI:
    '''
        This class is used by the clients to communicate with the server.
    '''

    # connection needed decorator
    def connection_needed(func):
        def wrapper(self, *args, **kwargs):
            if not self.is_connected:
                raise Exception("Not connected to the server")
            return func(self, *args, **kwargs)
        return wrapper

    def __init__(self):
        self.is_connected = False
        self.children = []
        
    def connect(self):
        print(f"\n\nMOCK SERVERAPI\n\nConnected to *** MOCK SERVER API ***")
        self.is_connected = True




    def build_request(self, service, command, *args):
        '''
            This method is used to build the request to be sent to the server.
        '''
        return None


# AUTHENTICATION -----------------------------------------------------------------------------------------------------
    @connection_needed
    def login(self, email, password):
        return True
    
    @connection_needed
    def signup(self, email, password, username):
        return True
    
    @connection_needed
    def new_agent_request(self, mac_address):
        return "mockserverapi: new_agent_request"
# ---------------------------------------------------------------------------------------------------------------------


# FETCHING INFORMATION -----------------------------------------------------------------------------------------------
    @connection_needed
    def get_info(self):
        raise "Shouldnt be used get_info servermockapi"
        pass

    @connection_needed
    def get_statistics(self):
        return "mockserverapi: get_statistics"
    
    @connection_needed
    def get_restrictions(self, child_name):
        return "mockserverapi: get_restrictions"


    @connection_needed
    def get_children(self):
        self.children = ["child1", "child2", "child3"]
        return ["mockserverapi: get_children"]
        

# ---------------------------------------------------------------------------------------------------------------------


# CHILDREN MANAGEMENT -----------------------------------------------------------------------------------------------
    @connection_needed
    def confirm_agent(self, auth_str, child_name):
        return "mockserverapi: confirm_agent"