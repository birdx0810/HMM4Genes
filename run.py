import logging

from model import MarkovOrderZero, MarkovOrderOne, MarkovOrderTwo

def main():
    logging.basicConfig(level=logging.INFO,
            format='\n%(asctime)s %(name)-5s === %(levelname)-5s === %(message)s\n')

    # read sequence
    seq_file_path = "./NC_000006_12_Homo_sapiens_chromosome_6_GRCh38_p13_Primary_Assembly.txt"
    with open(seq_file_path, 'r') as f:
        s = f.readline()
        s = s.strip('\n')
        s = s.lower()
    
    assert len(s) == 100000

    # run Markov models
    model_infos = {
        'Markov Model Order 0':{
            'class': MarkovOrderZero,
        },
        'Markov Model Order 1':{
            'class': MarkovOrderOne,
        },
        'Markov Model Order 2':{
            'class': MarkovOrderTwo,
        },
    }

    for model_name in model_infos.keys():
        print(f'\n=== {model_name} ===')
        model = model_infos[model_name]['class'](vocab=set(s), random_seed=17)
        model.fit(s)
        generated_seq = model.generate(len(s))
        # print(f'Generated sequence: {generated_seq}')
        print(f'Target sequence generation probability: {model.generating_prob(s)}')

    # TODO: run hidden Markov models
    
    return

if __name__ == '__main__':
    main()