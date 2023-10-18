function positionalStats(position, id) {
    switch(position) {
        case "C":
          return (<CenterStats id={id}></CenterStats>)
        case "RB":
          return (<RunningBackStats id={id}></RunningBackStats>)
        case "FB":
          return (<FullbackStats id={id}></FullbackStats>)
        case "HB":
          return (<HalfbackStats id={id}></HalfbackStats>)
        case "OG":
          return (<OffensiveGuardStats id={id}></OffensiveGuardStats>)
        case "OT":
          return (<OffensiveTackleStats id={id}></OffensiveTackleStats>)
        case "LG":
          return (<LeftGuardStats id={id}></LeftGuardStats>)
        case "LT":
          return (<LeftTackleStats id={id}></LeftTackleStats>)
        case "RG":
          return (<RightGuardStats id={id}></RightGuardStats>)
        case "RT":
          return (<RightTackleStats id={id}></RightTackleStats>)
        case "TE":
          return (<TightEndStats id={id}></TightEndStats>)
        case "QB":
          return (<QuarterbackStats id={id}></QuarterbackStats>)
        case "WR":
          return (<WideReceiverStats id={id}></WideReceiverStats>)
        case "CB":
        return (<CornerbackStats id={id}></CornerbackStats>)
        case "DE":
        return (<DefensiveEndStats id={id}></DefensiveEndStats>)
        case "DT":
        return (<DefensiveTackleStats id={id}></DefensiveTackleStats>)
        case "LB":
        return (<LinebackerStats id={id}></LinebackerStats>)
        case "ILB":
        return (<InsideLinebackerStats id={id}></InsideLinebackerStats>)
        case "MLB":
        return (<MiddleLinebackerStats id={id}></MiddleLinebackerStats>)
        case "NT":
        return (<NoseTackleStats id={id}></NoseTackleStats>)
        case "OLB":
        return (<OutsideLinebackerStats id={id}></OutsideLinebackerStats>)
        case "S":
        return (<SafetyStats id={id}></SafetyStats>)
        case "FS":
        return (<FreeSafetyStats id={id}></FreeSafetyStats>)
        case "SS":
        return (<StrongSafetyStats id={id}></StrongSafetyStats>)  
        case "K":
            return (<KickerStats id={id}></KickerStats>)
        case "KR":
            return (<KickReturnerStats id={id}></KickReturnerStats>)
        case "LS":
            return (<LongSnapperStats id={id}></LongSnapperStats>)
        case "P":
            return (<PunterStats id={id}></PunterStats>)
        case "PR":
            return (<PuntReturnerStats id={id}></PuntReturnerStats>)
        default:
            return null; // Handle any other cases if necessary
      }
      
}

export default function PlayerPage(props) {
    return (
    <div className="player">
        <img src={props.player_src} alt={props.name}/>
        <div className="caption">{props.name}</div>
        <div className="about">
            <div className="team">
                {props.team}{' '}-{' '}<span>{props.abbreviation}</span>
            </div>
            <div className="position">
                {props.position}
            </div>
        </div>
        <div className="stats">
            {positionalStats(props.position, props.id)}
        </div>
    </div>
    );
}