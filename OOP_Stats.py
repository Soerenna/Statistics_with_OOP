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
    
     def iqr(self,dec=None,local=False): # this method calculates the interquartile range
        
        tup = sorted(self.data)

        if len(tup) % 2 == 0: # if iterable is even
            median = (tup[int(len(tup)/2)] + tup[int(len(tup)/2 -1)])/2 # calculate median 

            first_half = tup[:int(len(tup)/2)] # slice the iterable into first- and second half
            second_half = tup[int(len(tup)/2):]

            if len(first_half) % 2 == 0: # check parity first half
                first_median = (first_half[int(len(first_half)/2)] + first_half[int(len(first_half)/2 -1)])/2 
                second_median = (second_half[int(len(second_half)/2)] + second_half[int(len(second_half)/2 -1)])/2

                IQR = second_median - first_median #calculate IQR
            else:
                first_median = first_half[int(len(first_half)/2-0.5)]
                second_median = second_half[int(len(second_half)/2-0.5)]

                IQR = second_median - first_median

        else: # if iterable is odd
            median = tup[int(len(tup)/2-0.5)]

            first_half = tup[:int(len(tup)/2-0.5)]
            second_half = tup[int(len(tup)/2-0.5 +1):]

            if len(first_half) % 2 == 0: # check parity first half

                first_median = (first_half[int(len(first_half)/2)] + first_half[int(len(first_half)/2 -1)])/2 
                second_median = (second_half[int(len(second_half)/2)] + second_half[int(len(second_half)/2 -1)])/2

                IQR = second_median - first_median
            else:

                first_median = first_half[int(len(first_half)/2-0.5)]
                second_median = second_half[int(len(second_half)/2-0.5)]

                IQR = second_median - first_median
            
        if dec != None:
                IQR = round(IQR,dec)

        return IQR if local else f'The IQR for {self.name} is {IQR}.'
