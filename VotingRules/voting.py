def dictatorship(preferences, agent):
    """
    Determines the winner based on the dictatorship rule.

    :param preferences: The preference object containing candidates and voters data.
    :type preferences: Preference
    :param agent: The agent (voter) who acts as the dictator.
    :type agent: int
    :return: The winning candidate chosen by the dictator.
    :rtype: int
    :raises ValueError: If the agent is not a valid voter.
    """
    if agent not in preferences.voters():
        raise ValueError("Invalid agent")
    # Loop through candidates to find the one ranked highest by the dictator (agent)
    for candidate in preferences.candidates():
        if preferences.get_preference(candidate, agent) == 0:
            return candidate

def scoring_rule(preferences, score_vector, tie_break_agent):
    """
    Determines the winner based on a scoring rule, with possible tie-breaking.

    :param preferences: The preference object containing candidates and voters data.
    :type preferences: Preference
    :param score_vector: A list defining the scoring rule for each rank.
    :type score_vector: List[int]
    :param tie_break_agent: The agent used for tie-breaking when needed.
    :type tie_break_agent: int
    :return: The winning candidate based on the scoring rule.
    :rtype: int
    :raises ValueError: If the score vector's length does not match the number of candidates.
    """
    if len(score_vector) != len(preferences.candidates()):
        raise ValueError("The score vector's length must be equal to the number of candidates.")

    # Initialize score dictionary for each candidate
    total_score_of_candidate = {candidate : 0 for candidate in preferences.candidates()}
    score_vector = sorted(score_vector, reverse=True)
    # Calculate total score for each candidate based on each voter's ranking
    for voter in preferences.voters():
        for candidate in preferences.candidates():
            rank = preferences.get_preference(candidate, voter)
            total_score_of_candidate[candidate] += score_vector[rank]

    # Find the highest score among candidates
    highest_score = max(total_score_of_candidate.values())
    tie_candidates = []
    for candidate, score in total_score_of_candidate.items():
        if score == highest_score:
            tie_candidates.append(candidate)

    # If there is a tie, use tie-break agent's preference to determine the winner
    if len(tie_candidates) > 1:
        tie_candidate_ranks = []
        for candidate in tie_candidates:
            rank = preferences.get_preference(candidate, tie_break_agent)
            tie_candidate_ranks.append((candidate, rank))

        min_rank = min([rank for candidate, rank in tie_candidate_ranks])

        # Return the candidate with the lowest rank according to tie_break_agent's preference
        for candidate, rank in tie_candidate_ranks:
            if rank == min_rank:
                return candidate
    else:
        # If only one candidate has the highest score, return that candidate
        return tie_candidates[0]


def plurality(preferences, tie_break):
    """
    Determines the winner using the plurality rule, with possible tie-breaking.

    :param preferences: The preference object containing candidates and voters data.
    :type preferences: Preference
    :param tie_break: The agent used for tie-breaking in case of a tie.
    :type tie_break: int
    :return: The winning candidate based on the plurality rule.
    :rtype: int
    """
    # Initialize vote count for each candidate
    total_score_of_candidates = {candidate : 0 for candidate in preferences.candidates()}

    # Tally votes for each candidate based on who is ranked first by each voter
    for voter in preferences.voters():
        for candidate in preferences.candidates():
            if preferences.get_preference(candidate, voter) == 0:
                total_score_of_candidates[candidate] += 1

    # Find the candidate(s) with the highest number of votes
    highest_score = max(total_score_of_candidates.values())
    tie_candidates = []
    for candidate, score in total_score_of_candidates.items():
        if score == highest_score:
            tie_candidates.append(candidate)

    # Resolve tie if needed
    if len(tie_candidates) > 1:
        tie_candidate_ranks = []

        for candidate in tie_candidates:
            rank = preferences.get_preference(candidate, tie_break)
            tie_candidate_ranks.append((candidate, rank))

        min_rank = min([rank for candidate, rank in tie_candidate_ranks])

        for candidate, rank in tie_candidate_ranks:
            if rank == min_rank:
                return candidate

    else:
        return tie_candidates[0]

def veto(preferences, tie_break):
    """
    Determines the winner using the veto rule, with possible tie-breaking.

    :param preferences: The preference object containing candidates and voters data.
    :type preferences: Preference
    :param tie_break: The agent used for tie-breaking in case of a tie.
    :type tie_break: int
    :return: The winning candidate based on the veto rule.
    :rtype: int
    """
    total_score_of_candidates = {candidate: 0 for candidate in preferences.candidates()}
    candidate_counts = len(preferences.candidates())

    # Award 1 point to all candidates except the one ranked last by each voter
    for voter in preferences.voters():
        for candidate in preferences.candidates():
            if preferences.get_preference(candidate, voter) != candidate_counts - 1:
                total_score_of_candidates[candidate] += 1

    # Find the candidate(s) with the highest total score
    highest_score = max(total_score_of_candidates.values())
    tie_candidates = []
    for candidate, score in total_score_of_candidates.items():
        if score == highest_score:
            tie_candidates.append(candidate)

    # Resolve tie using tie-breaking agent's preference
    if len(tie_candidates) > 1:

        tie_candidate_ranks = []

        for candidate in tie_candidates:
            rank = preferences.get_preference(candidate, tie_break)
            tie_candidate_ranks.append((candidate, rank))

        min_rank = min([rank for candidate, rank in tie_candidate_ranks])

        for candidate, rank in tie_candidate_ranks:
            if rank == min_rank:
                return candidate

    else:
        return tie_candidates[0]

def borda(preferences, tie_break):
    """
    Determines the winner using the Borda count rule, with possible tie-breaking.

    :param preferences: The preference object containing candidates and voters data.
    :type preferences: Preference
    :param tie_break: The agent used for tie-breaking in case of a tie.
    :type tie_break: int
    :return: The winning candidate based on the Borda count rule.
    :rtype: int
    """
    total_score_of_candidates = {candidate: 0 for candidate in preferences.candidates()}
    candidate_counts = len(preferences.candidates())

    # Calculate Borda score for each candidate based on each voter's ranking
    for voter in preferences.voters():
        for candidate in preferences.candidates():
            rank = preferences.get_preference(candidate, voter)
            total_score_of_candidates[candidate] += candidate_counts - 1 - rank

    # Find the candidate(s) with the highest Borda score
    highest_score = max(total_score_of_candidates.values())
    tie_candidates = []
    for candidate, score in total_score_of_candidates.items():
        if score == highest_score:
            tie_candidates.append(candidate)

    # Resolve tie if necessary
    if len(tie_candidates) > 1:

        tie_candidate_ranks = []

        for candidate in tie_candidates:
            rank = preferences.get_preference(candidate, tie_break)
            tie_candidate_ranks.append((candidate, rank))

        min_rank = min([rank for candidate, rank in tie_candidate_ranks])

        for candidate, rank in tie_candidate_ranks:
            if rank == min_rank:
                return candidate

    else:
        return tie_candidates[0]

def STV(preferences, tie_break):
    """
    Determines the winner using the Single Transferable Vote (STV) rule.

    :param preferences: The preference object containing candidates and voters data.
    :type preferences: Preference
    :param tie_break: The agent used for tie-breaking in case of a tie.
    :type tie_break: int
    :return: The winning candidate based on the STV rule.
    :rtype: int
    """
    remain_candidates = preferences.candidates()

    while len(remain_candidates) > 1:
        total_score_of_candidates = {candidate: 0 for candidate in remain_candidates}

        # Tally first-choice votes for remaining candidates
        for voter in preferences.voters():
            for candidate in remain_candidates:
                if preferences.get_preference(candidate, voter) == 0:
                    total_score_of_candidates[candidate] += 1

                    break

        # Identify candidate(s) with the fewest votes
        min_score = min(total_score_of_candidates.values())
        least_scorers = []
        for candidate, score in total_score_of_candidates.items():
            if score == min_score:
                least_scorers.append(candidate)

        # Handle ties for elimination using tie-breaking agent's preference
        if len(least_scorers) > 1:
            tie_candidate_ranks = []

            for candidate in least_scorers:
                rank = preferences.get_preference(candidate, tie_break)
                tie_candidate_ranks.append((candidate, rank))

            max_rank = max([rank for candidate, rank in tie_candidate_ranks])

            # Eliminate the candidate that tie_break agent ranks the lowest
            for candidate, rank in tie_candidate_ranks:
                if rank == max_rank:
                    remain_candidates.remove(candidate)
                    break

        else:
            # Eliminate the single candidate with the fewest votes
            remain_candidates.remove(least_scorers[0])

    # Return the last remaining candidate as the winner
    return remain_candidates[0]









