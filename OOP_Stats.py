class Stat_Object:
    
    # this class will create an object containing data points and will allow the user to call statistics or parameters on it
    
    def __init__(self, name, *args,scope='unknown'):
    
        self.name = name
        self.data = args
        self.total = len(args)
        self.scope = 'unknown'
    
    # special methods
    
    def __str__(self):
        return f'{self.name}: {self.data}'
        
    # here are the user-defined methods for the data
    # the 'local' parameter will determine the output of the function i.e. if true it wil output a value, when false it outputs a string
    
    def mean(self,dec=None):
        
        mu = sum(self.data)/self.total
        if dec != None:
            mu = round(mu,dec)
        
        return f'the mean is {mu}'
    
    def population_variance(self,dec=None):
    
   
        mu = sum(self.data)/self.total
        sq_devs = [(i-mu)**2 for i in self.data]
        variance = (sum(sq_devs)) / self.total
        
        if dec != None:
            variance = round(variance,dec)
        
        return f'the population variance for {self.name} is {variance}'

    
    def population_sd(self,dec=None,local=False):
        
        from math import sqrt
        tup = self.data
        
        def pop_var(tup):
            mu = sum(tup)/len(tup)
            sq_devs = [(i-mu)**2 for i in tup]
            variance = (sum(sq_devs)) / len(tup)
            return variance
        
        sd = sqrt(pop_var(tup))
        
        if dec != None:
            sd = round(sd,dec)

        return sd if local == True else f'the population standard deviation for {self.name} is {sd}'
    
    def sample_variance(self,dec=None):
        
    
        # calculate the mean and assign to variable
        
        tup = self.data
        
        xbar = sum(tup)/self.total
        # for each data-point calculate the deviations, square- and store them
        sq_devs = [(i-xbar)**2 for i in tup]
        # sum the stored squared deviations
        # divide by number of data points
        variance = (sum(sq_devs)) / (self.total-1)
        
        if dec != None:
            variance = round(variance,dec)

        return f'the sample variance for {self.name} is {variance}'
    
    def sample_sd(self,dec=None,local=False):
    
        from math import sqrt
        tup = self.data
        
        def sample_var(tup): 

            xbar = sum(tup)/len(tup)
            sq_devs = [(i-xbar)**2 for i in tup]
            variance = (sum(sq_devs)) / (len(tup)-1)
            return variance
        
        sd = sqrt(sample_var(tup)) # take root of sample variance
        
        if dec != None:
            sd = round(sd,dec)
            
        return sd if local == True else f'the sample standard deviation for {self.name} is {sd}'
