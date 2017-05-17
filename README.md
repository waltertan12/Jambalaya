# Jambalaya
Jambalaya is an app that simplifies decision making with brackets

## Schema
```
User

COLUMN         TYPE
id             INT
email          VARCHAR
passwordDigest VARCHAR
userType       VARCHAR   DEFAULT 'user'
createdDate    DATETIME
modifiedDate   DATETIME
```

```
UserAttribute

COLUMN         TYPE
id             INT
userId         INT       References User.id
attributeName  VARCHAR
attributeValue VARCHAR
createdDate    DATETIME
modifiedDate   DATETIME
```

```
Team
This can be a restaurant or an activity

COLUMN         TYPE
id             INT
name           VARCHAR
pointsFor      INT
pointsAgainst  INT
createdDate    DATETIME
modifiedDate   DATETIME
```

```
TeamAttribute

COLUMN          TYPE
id              INT
teamId          INT      References team.id
attributeName   VARCHAR
attributeValue  VARCHAR
createdDate     DATETIME
modifiedDate    DATETIME

UNIQUE KEY (playerId, attributeName)
```

```
Tournament

COLUMN         TYPE
id             INT
tournamentType VARCHAR
createdDate    DATETIME
modifiedDate   DATETIME
```

```
Round

COLUMN         TYPE
id             INT
tournamentId   INT      References Tournament.id
roundNumber    INT
status         VARCHAR
createdDate    DATETIME
modifiedDate   DATETIME
```

```
Match

COLUMN         TYPE
id             INT
roundId        INT      References Round.id
teamOneId      INT      References Team.id
teamTwoId      INT      References Team.id
teamOneScore   INT
teamTwoScore   INT
createdDate    DATETIME
modifiedDate   DATETIME
```

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

