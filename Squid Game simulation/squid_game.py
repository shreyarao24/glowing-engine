import random
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

col_names = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5', 'Player 6', 'Player 7', 'Player 8', 'Player 9', 'Player 10', 'Player 11', 'Player 12', 'Player 13', 'Player 14', 'Player 15', 'Player 16']

full_runs = pd.DataFrame(columns = col_names)

for r in range(0, 10):

    all_steps = []
    completed = []

    for p in range(0, 16):

        if p == 0:
            steps = []
            for s in range(0, 18):
                step = random.randint(0, 1)

                if step == 1:
                    steps.append(step)
                else:
                    all_steps.append(steps)
                    completed.append(len(steps))
                    break

        else:
            steps = all_steps[p - 1] + [1]

            for s in range(len(steps) , 18):
                step = random.randint(0, 1)

                if step == 1:
                    steps.append(step)
                else:
                    all_steps.append(steps)
                    completed.append(len(steps))
                    break

        if len(steps) == 18:
            completed.append(len(steps))
            all_steps.append(steps)
            break

    last_completed = completed.index(completed[-1])

    if len(completed) < 16:
        for i in range(last_completed + 1, 16):
            completed.append(18)

    full_runs.loc[len(full_runs.index)] = completed

nums_successful = {}

for p in col_names:
    nums_successful[p] = full_runs[p].tolist().count(18)

nums_df = pd.DataFrame.from_dict(nums_successful, orient = 'index')
nums_df.rename(columns = {0:'frequency'}, inplace=True)
nums_df['probability'] = nums_df['frequency']/10
nums_df['players'] = col_names

plt.bar(nums_df['players'], nums_df['probability'])
plt.xticks(rotation = 90)
plt.ylabel('Frequency of success')
plt.tick_params(axis='x', which='major', labelsize=7)
plt.show()