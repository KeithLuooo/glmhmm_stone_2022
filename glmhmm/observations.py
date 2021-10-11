#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:38:30 2020

@author: istone
"""

import autograd.numpy as np
#import jax.numpy as jnp

class Observations(object):
    
    def __init__(self,n,m,c):
       self.n, self.m, self.c = n, m, c
        
class BernoulliObservations(object):
    
    def __init__(self,n,m,c):
        self.n, self.m, self.c = n, m, c
    
    def compObs(self,x,w,normalize=True):
        """
        Computes the GLM observation probabilities for each data point.

        Parameters
        ----------
        x : nxm array of the data (design matrix)
        w : mxc array of weights
        normalize : boolean, optional
            Determines whether or not observation probabilities are normalized. The default is True.

        Returns
        -------
        phi : nxc array of the observation probabilities

        """
        
        assert self.c == 2, "A Bernoulli distribution must only have two observation classes (c=2)"
        
        phi = np.exp(x@w) # get exponentials e^(wTx)
        if normalize:
            phi = np.divide(phi.T,np.sum(phi,axis=1)).T # normalize the exponentials 
        
        return phi
    
class MultinomialObservations(object):
    
    def __init__(self,n,m,c):
        self.n, self.m, self.c = n, m, c
    
    def compObs(self,x,w,normalize=True):
        """
        Computes the GLM observation probabilities for each data point.

        Parameters
        ----------
        x : nxm array of the data (design matrix)
        w : mxc array of weights
        normalize : boolean, optional
            Determines whether or not observation probabilities are normalized. The default is True.

        Returns
        -------
        phi : nxc array of the observation probabilities

        """
        
        assert self.c > 2, "A multinomial distribution should have more than two observation classes (c>2)"
        
        phi = np.exp(x@w) # get exponentials e^(wTx)
        if normalize:
            phi = np.divide(phi.T,np.sum(phi,axis=1)).T # normalize the exponentials 
        
        return phi