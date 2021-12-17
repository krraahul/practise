package main

type Int int64

func IsFeedingPossible(animals string, dogFoodStock Int, catFoodStock Int, bonusCatFood Int) bool {
	for _, animal := range animals {
		if animal == 'D' {
			if dogFoodStock == 0 || catFoodStock < 0 {
				return false
			}
			dogFoodStock--
			catFoodStock += bonusCatFood
		} else if animal == 'C' {
			catFoodStock--
		}
	}

	return true
}
