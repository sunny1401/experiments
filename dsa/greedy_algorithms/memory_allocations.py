from typing import List, Dict


def first_fit(process_size: List, memory: List) -> Dict:

    process_memory = {i: 0 for i in process_size}

    for process in process_size:
        for i in range(0, len(memory)):
            if memory[i] >= process:
                process_memory[process] = (i + 1, memory[i])
                memory[i] = memory[i] - process
                break

    return process_memory


def worst_fit(process_size: List, memory: List) -> Dict:

    process_memory = {i: 0 for i in process_size}

    for process in process_size:
        id_associated = -1
        for i in range(0, len(memory)):
            if memory[i] >= process:
                if id_associated == -1 or memory[id_associated] < memory[i]:
                    process_memory[process] = (i + 1, memory[i])
                    id_associated = i

            if id_associated != -1:
                memory[id_associated] = memory[id_associated] - process

    return process_memory


def best_fit(process_size: List, memory: List) -> Dict:
    process_memory = {i: 0 for i in process_size}

    for process in process_size:
        id_associated = -1
        for i in range(0, len(memory)):
            if memory[i] >= process:
                if id_associated == -1 or memory[id_associated] > memory[i]:
                    process_memory[process] = (i + 1, memory[i])
                    id_associated = i

        if id_associated != -1:
            memory[id_associated] = memory[id_associated] - process

    return process_memory
