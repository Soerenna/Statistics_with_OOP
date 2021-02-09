class Stat_Object:
    
    # this class will create an object containing data points and will allow the user to call statistics or parameters on it
    
    def __init__(self, name, *args,scope='unknown'):
    
        self.name = name # name of dataset
        self.data = args # the dataset
        self.total = len(args) # number of datapoints
        self.scope = 'unknown' # wheter the dataset is a population or a sample
    
    # special methods
    
    def __str__(self):
        return f'{self.name}: {self.data}'
        
    # here are the user-defined methods for the data
    # the 'local' parameter will determine the output of the function i.e. if true it wil output a value, when false it outputs a string
    # the 'custom' parameter will allow for custom data input in class methods
    def mean(self,dec=None):
        
        mu = sum(self.data)/self.total
        if dec != None:
            mu = round(mu,dec)
        
        return f'the mean is {mu}'
    
    def median(self,dec=None,local=False,custom=False):
        
        """return the median of an iterable
            dec: determines how to output is rounded
            local: if it is set to True the output wil be a number instead of string
            custom: allows for custom data input instead of class instance data
            
            e.g. median([1,2,3],local=True) --> 2"""
        
        if custom:
            x = custom
        else:
            x = self.data
        if len(x) % 2 == 0:
            i = int(len(x)/2)
            median = (x[i-1]+x[i])/2
        else:
            median = x[int((len(x)-1)/2)]  
        if dec != None:
            median = round(median,dec)
        return median if local else f'the median of {self.name} is {median}'
    
    def population_variance(self,dec=None,local=False):
    
        mu = sum(self.data)/self.total # calculate the mean and assign to variable
        sq_devs = [(i-mu)**2 for i in self.data] # for each datapoint calculate the deviations, square and store them
        variance = (sum(sq_devs)) / self.total # sum the stored squared deviations and divide by the # of datapoints 
        
        if dec != None:
            variance = round(variance,dec)
        
        return variance if local else f'the population variance for {self.name} is {variance}'

    
    def population_sd(self,dec=None,local=False):
        
        from math import sqrt
        tup = self.data
        
        pop_var = self.population_variance(local=True)
        
        sd = sqrt(pop_var) # take root of population variance
        
        if dec != None:
            sd = round(sd,dec)

        return sd if local == True else f'the population standard deviation for {self.name} is {sd}'
    
    def sample_variance(self,dec=None,local=False):
        
        # calculate the mean and assign to variable
        
        tup = self.data
        
        xbar = sum(tup)/self.total
        
        sq_devs = [(i-xbar)**2 for i in tup] # for each data-point calculate the deviations, square- and store them

        variance = (sum(sq_devs)) / (self.total-1) # sum the stored squared deviations and divide by number of data point
        
        if dec != None:
            variance = round(variance,dec)

        return variance if local else f'the sample variance for {self.name} is {variance}'
    
    def sample_sd(self,dec=None,local=False):
    
        from math import sqrt
        tup = self.data
        
        sample_var = self.sample_variance(local=True)
        
        sd = sqrt(sample_var) # take root of sample variance
        
        if dec != None:
            sd = round(sd,dec)
            
        return sd if local == True else f'the sample standard deviation for {self.name} is {sd}'
    
    def iqr(self,dec=None,local=False,custom=False):
        
        """return the inter quartile range of an iterable
            dec: determines how to output is rounded
            local: if it is set to True the output wil be a number instead of string
            custom: allows for custom data input instead of class instance data
            
            e.g. iqr([1,2,3,4,5,6,7],local=True) --> 4.0"""
    
        def splitter(X):
            if len(X) % 2 == 0:
                i = int(len(X)/2)
                first_half = X[:i]
                second_half = X[i:]
            else:
                i = int(len(X)//2)
                first_half = X[:i]
                second_half = X[i+1:]

            return (first_half,second_half)
        
        if custom:
            S = sorted(custom)
        else:
            S = sorted(self.data)
        
        q1 = self.median(custom=splitter(S)[0],local=True)
        q3 = self.median(custom=splitter(S)[1],local=True)

        iqr = q3 - q1
        
        if dec != None:
            iqr = round(iqr,dec)
        
        return iqr if local else f'The inter quartile range for {self.name} is {iqr}'

    def MAD(self,dec=None,local=False): 
        
        """return the mean absolute deviation of an iterable
            dec: determines how to output is rounded
            local: if it is set to True the output wil be a number instead of string
            
            e.g. MAD([1,2,3,4],local=True) --> 1.0 """
    
        absolute_deviations = []

        mean = sum(self.data)/len(self.data) 

        for data_point in self.data:

            absolute_deviations.append(abs(data_point-mean)) # take absolute deviation for every datapoint

        mad = (sum(absolute_deviations))/self.total # sum them and divide by number of points
        
        if dec != None:
                mad = round(mad,dec)


        return mad if local else f'The MAD for {self.name} is {mad}'
    
    def z_score(self,datapoint=0,dec=None,local=False):
        
        """return the z-score (standard score) of a datapoint inside the dataset
            datapoint: the datapoint you wish to calculate the z-score for
            dec: determines how to output is rounded
            local: if it is set to True the output wil be a number instead of string
            custom: allows for custom data input instead of class instance data
            
            e.g. if data = [1,2,3,4] then z_score(datapoint=3,local=True,round=2) --> 0.45"""
        
        scope_range = 'ps'
        scope = ' '
        
        mu = sum(self.data)/self.total
        
        while not scope in scope_range: # ask for user input concerning scope of data
            
            scope = input('Is your data set a Population(p) or a Sample(s)?: ').lower() 
            if not scope in 'ps':
                print('Please enter either p or s.')
        
        if scope == 'p': # save this information about datset in attributes
            self.scope = 'Population' 
        else:
            self.scope = 'Sample'
            
            
        pop_z_score = (datapoint - mu)/self.population_sd(local=True) # calculate z-scores
        samp_z_score = (datapoint - mu)/self.sample_sd(local=True)
        
        if dec != None:
            pop_z_score = round(pop_z_score,dec)
            samp_z_score = round(samp_z_score,dec)
            
        if local:
            return pop_z_score if scope == 'p' else samp_z_score
        else:
            if scope == 'p':
                return f'The population z-score for point {datapoint} is {pop_z_score}'
            else:
                return f'The sample z-score for point {datapoint} is {samp_z_score}'
