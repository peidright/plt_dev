#include "fea.h"
#include "fea_type.h"
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <ga/ga.h>
#include <ga/std_stream.h>

using namespace std;

#define cout STD_COUT
#define ostream STD_OSTREAM

float objective(GAGenome &);


int ga_fea_init()
{
    vector<fea *> vfea;
    for(int i=0;i<10;i++) {
        new fea(FEA_NULL,i);
        //vfea.push_back(new fea(FEA_NULL,i));
    }
    return 0;
}


int ga_fea_work()
 {
  GAParameterList params;
  GASteadyStateGA::registerDefaultParameters(params);
  params.set(gaNpopulationSize, 30);	// population size
  params.set(gaNpCrossover, 0.6);	// probability of crossover
  params.set(gaNpMutation, 0.01);	// probability of mutation
  params.set(gaNnGenerations, 1000);	// number of generations
  params.set(gaNpReplacement, 0.5);	// how much of pop to replace each gen
  params.set(gaNscoreFrequency, 10);	// how often to record scores
  params.set(gaNnReplacement, 4);	// how much of pop to replace each gen
  params.set(gaNflushFrequency, 10);	// how often to dump scores to file
  params.set(gaNscoreFilename, "bog.dat");
  //params.read("settings.txt");	        // grab values from file first
  //params.parse(argc, argv, gaFalse); // parse command line for GAlib args
 }


