####
# Each team's file must define four tokens:
#     team_name: WE HAVE NO CREATIVITY
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.my_score, their_score are ints.Make my move.Returns 'c' or 'b'. '''
    if len(my_history)%3==0:
        return'b'
    elif my_history[-1]=='b' and their_history[-1]=='b':
        return'b'
    else:
        return 'b'
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)from this module. Prints error if return value != result.Returns True or False, dpending on whether result was as expected.'''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     

    if test_move(my_history='',their_history='',my_score=0,their_score=0,result='b'):
         print 'Test passed'

    test_move(my_history='bbb',their_history='ccc',my_score=0,their_score=0,result='b')  