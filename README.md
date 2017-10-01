# Jambalaya
Jambalaya is an app that simplifies decision making with brackets

## Schema
### User
| Column Name     | Data Type | Notes       |
|-----------------|-----------|-------------|
| id              | INT       | Primary key |
| email           | VARCHAR   | Unique key  |
| password_digest | VARCHAR   |             |
| user_type       | INT       |             |
| created_date    | DATETIME  |             |
| modified_date   | DATETIME  |             |

### UserAttribute
| Column Name     | Data Type | Notes       |
|-----------------|-----------|-------------|
| id              | INT       | Primary key |
| user_id         | INT       | Foreign key |
| attribute_name  | VARCHAR   |             |
| attribute_value | VARCHAR   |             |
| created_date    | DATETIME  |             |
| modified_date   | DATETIME  |             |

### Player
| Column Name     | Data Type | Notes       |
|-----------------|-----------|-------------|
| id              | INT       | Primary key |
| name            | VARCHAR   |             |

### PlayerAttribute
| Column Name     | Data Type | Notes       |
|-----------------|-----------|-------------|
| id              | INT       | Primary key |
| player_id       | INT       | Foreign key |
| attribute_name  | VARCHAR   |             |
| attribute_value | VARCHAR   |             |
| created_date    | DATETIME  |             |
| modified_date   | DATETIME  |             |

Planning to use this table to store Google Place API data or Yelp API data

### Tournament
| Column Name       | Data Type | Notes       |
|-------------------|-----------|-------------|
| id                | INT       | Primary key |
| number_of_rounds  | INT       |             |

### TournamentType
| Column Name       | Data Type | Notes       |
|-------------------|-----------|-------------|
| id                | INT       | Primary key |
| tournament_type   | VARCHAR   |             |

Not necessary yet but might be able to support more than just single elimination

### Registration
| Column Name       | Data Type | Notes       |
|-------------------|-----------|-------------|
| id                | INT       | Primary key |
| player_id         | INT       | Foreign key |
| registration_date | DATETIME  |             |

### PlayingIn
| Column Name       | Data Type | Notes       |
|-------------------|-----------|-------------|
| id                | INT       | Primary key |
| registration_id   | INT       | Foreign key |
| seed              | INT       |             |

Decouples player from the tournament. Allows us to keep track of how often a player is used in tournaments.

### Fixture
| Column Name                | Data Type | Notes       |
|----------------------------|-----------|-------------|
| id                         | INT       | Primary key |
| first_registration_id      | INT       | Foreign key |
| second_registration_id     | INT       | Foreign key |
| round                      | INT       |             |
| first_registration_points  | INT       |             | 
| second_registration_points | INT       |             | 

### FixtureResult
| Column Name                | Data Type | Notes       |
|----------------------------|-----------|-------------|
| id                         | INT       | Primary key |
| winning_registration_id    | INT       | Foreign key |

## Services
Would like to something slightly more different than normal MVC since I seemed to struggled with keeping domain logic in the model in the Timeline app

Instead, I want to try an [anemic domain model](https://en.wikipedia.org/wiki/Anemic_domain_model) and keep most of the logic in a Service layer.
 
- TournamentService: These should all return a Tournament object
	- `#createTournament()`
	- `#addTeam(tournament, teamData)`
		- Calls TeamService#createTeam
	- `#removeTeam(tournament, team)`
	- `#vote(tournament, team)`

- TeamService: These should all return a Team object
	- `#createTeam()`
	- `#updateTeam(team)`
	- `#deleteTeam(team)`

- SocketService: Should return Promise? Can also try some FRP and use streams instead
	- `#on(eventName)`
	- `#emit(eventName)`

- UserService
	- `#createUser()`
	- `#updateUser(user)`
	- `#deleteUser(user)`

- SessionService
	- `#createSession(credentials)`
	- `#deleteSession(user)`

- TrackingService: Should handle all tracking?

## Constants
- SocketEvents
	- `addTeam`
	- `removeTeam`
	- `vote`

