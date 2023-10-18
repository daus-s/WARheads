create table Rosters (  year INT unsigned,     team CHAR (3),     pos1 INT,  pos2 INT,  pos3 INT,  pos4 INT,  pos5 INT,  pos6 INT,  pos7 INT,  pos8 INT,  pos9 INT,  pos10 INT,  pos11 INT,  pos12 INT,  pos13 INT,  pos14 INT,  pos15 INT,  pos16 INT,  pos17 INT,  pos18 INT,  pos19 INT,  pos20 INT,  pos21 INT,  pos22 INT,  pos23 INT,  pos24 INT,  pos25 INT,  pos26 INT,  pos27 INT,  pos28 INT,  pos29 INT,  pos30 INT,  pos31 INT,  pos32 INT,  pos33 INT,  pos34 INT,  pos35 INT,  pos36 INT,  pos37 INT,  pos38 INT,  pos39 INT,  pos40 INT,  pos41 INT,  pos42 INT,  pos43 INT,  pos44 INT,  pos45 INT,  pos46 INT,  pos47 INT,  pos48 INT,  pos49 INT,  pos50 INT,  pos51 INT,  pos52 INT,  pos53 INT,     id CHAR(7),     PRIMARY KEY (id) );
create table PASSING_nfl (
	id INT unsigned,
    primary key (id),
    PassingYards INT unsigned,
    YdsPerAtt FLOAT,
    Attempts INT, 
    Completions INT,
    CompletionPercent FLOAT, 
    TouchDowns INT, 
    Interceptions INT,
    PasserRating FLOAT, 
    FirstDowns INT, 
    FirstDownPercent FLOAT, 
    CompGT20 INT,
    CompGT40 INT, 
    LongestComp INT,
    Sacks INT, 
    YardsLostSacks INT
);
create table Players (  
	name VARCHAR(24) NOT NULL,     
    id INT unsigned ,     
    position CHAR (2),     
    PRIMARY KEY (id) 
);
create table Rushing_NFL (
	id INT unsigned,
    primary key (id),
	RushingYards INT unsigned,
    Att INT,
    Touchdowns INT,
    RushGT20 INT,
    RushGT40 INT, 
    LongestRush INT,
    RushingFD INT, 
    RushingFDpercentage FLOAT,
    RushingFumbles INT
);
CREATE TABLE Receiving_nfl (
	id INT unsigned,
    primary key (id),
    Receptions int,
    Yards INT,
    Touchdowns INT,
    RecGT20 INT,
    RecGT40 INT, 
    LongestRec INT,
    RecFD INT,
    FDpercentage FLOAT,
    RecFumble INT,
    RecYAC INT,
    Targets INT
);
CREATE TABLE Fumbles_nfl (
	id INT unsigned,
    primary key (id),
    ForcedFumble INT, 
    FumbleRecovery INT,
    FumbleRecoveryTD INT
);
CREATE TABLE Tackles_nfl (
	id INT unsigned,
    primary key (id),
    CombinedTackles INT,
    Assists INT,
    Solo INT,
    Sacks INT
);
CREATE TABLE Interceptions (
	id INT unsigned,
    primary key (id),
    Interceptions INT,
    PickSix INT, 
    InterceptionYards INT,
    LongestIntReturn INT
);
CREATE TABLE Fieldgoals_nfl (
	id INT unsigned,
    primary key (id),
    FGM INT,
    Att INT,
    FGpercent FLOAT,
    Made1_19 INT,
    Att1_19 INT,
    Made20_29 INT,
    Att20_29 INT,
    Made30_39 INT,
    Att30_39 INT,
    Made40_49 INT,
    Att40_49 INT,
    Made50_59 INT,
    Att50_59 INT,
    Made60plus INT,
    Att60plus INT, 
    LongestFG INT,
    FGBlocked INT
);
CREATE TABLE Kickoffs_nfl (
	id INT unsigned,
    primary key (id),
    Kickoffs INT, 
    Yards INT,
    ReturnYards INT, 
    Touchbacks INT,
    TouchbackPercent FLOAT,
    Ret INT, 
    RetAvg FLOAT,
    OnsideKick INT,
    OnsideKickRec INT,
    OutOfBounds INT,
    TouchdownReturns INT
);
CREATE TABLE kickoffreturns_nfl (
	id INT unsigned,
    primary key (id),
    Average FLOAT,
    Ret INT,
    Yards INT,
    KRetTD INT,
    RetGT20 INT,
    RetGT40 INT, 
    LongestReturn INT,
    FairCatch INT,
    Fumbles INT
);
CREATE TABLE punts_nfl (
	id INT unsigned,
    primary key (id),
	Average FLOAT,
    NetAvg FLOAT,
    NetYards INT,
    Punts INT,
    Longest INT,
    Yards INT,
    Inside20 INT, 
    OutOfBounds INT,
    Downed INT, 
    Touchback INT, 
    Faircatch INT, 
    Ret INT,
    RetYards INT, 
    Touchdowns INT, 
    PuntsBlocked INT
);
CREATE TABLE Puntreturns_nfl (
	id INT unsigned,
    primary key (id),
    Average FLOAT,
    Ret INT, 
    Yards INT, 
    PuntRetTDs INT,
    RetGT20 INT,
    RetGT40 INT,
    Longest INT,
    FairCatch INT, 
    Fumbles INT
);
