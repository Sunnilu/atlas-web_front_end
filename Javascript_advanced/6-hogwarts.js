class studentHogwarts {
    // Private variables
    #privateScore = 0;
    #name = null;

    // Private method to change score
    #changeScoreBy(points) {
        this.#privateScore += points;
    }

    // Public method to set the name
    setName(newName) {
        this.#name = newName;
        return this;
    }

    // Public method to reward the student (increase score by 1)
    rewardStudent() {
        this.#changeScoreBy(1);
        return this;
    }

    // Public method to penalize the student (decrease score by 1)
    penalizeStudent() {
        this.#changeScoreBy(-1);
        return this;
    }

    // Public method to get the student's score in the format: name: score
    getScore() {
        return `${this.#name}: ${this.#privateScore}`;
    }
}

// Creating Harry object
let harry = new studentHogwarts();
harry.setName('Harry');
harry.rewardStudent().rewardStudent().rewardStudent().rewardStudent();
console.log(harry.getScore()); // Output: Harry: 4

// Creating Draco object
let draco = new studentHogwarts();
draco.setName('Draco');
draco.rewardStudent();
draco.penalizeStudent().penalizeStudent().penalizeStudent();
console.log(draco.getScore()); // Output: Draco: -2
