# driver.py


import sys
from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

engine = knowledge_engine.engine(__file__)


def forwardChani():
    
    try:
        engine.reset()
        engine.activate('rules')

        with engine.prove_goal('rules.diagnosis($result)') as gen:
            for i, (vars, no_plan) in enumerate(gen):
                result = vars['result']
                total = result[0] + result[1] + result[2] + result[3]
                print ("Arthitis: ",  round(100*result[0]/total) , "% ")
                print ("Rash: ",  round(100*result[1]/total), "%  ")
                print ("Malaria: ", round( 100*result[2]/total), "% ")
                print ("Other: ",  round(100*result[3]/total), "%  ")



    except:
        krb_traceback.print_exc()
        sys.exit(1)


