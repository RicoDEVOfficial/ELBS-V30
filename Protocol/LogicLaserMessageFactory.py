from Protocol.Messages.Client.Other.EndClientTurnMessage import EndClientTurnMessage
from Protocol.Messages.Client.Login.ClientHelloMessage import ClientHelloMessage
from Protocol.Messages.Client.Login.LoginMessage import LoginMessage
from Protocol.Messages.Client.Other.KeepAliveMessage import KeepAliveMessage
from Protocol.Messages.Client.Other.AnalyticsEventMessage import AnalyticsEventMessage
from Protocol.Messages.Client.Other.SetNameMessage import SetNameMessage
from Protocol.Messages.Client.Team.TeamCreateMessage import TeamCreateMessage
from Protocol.Messages.Client.Team.TeamLeaveMessage import TeamLeaveMessage
from Protocol.Messages.Client.Team.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Protocol.Messages.Client.Team.TeamToggleSettingsMessage import TeamToggleSettingsMessage
from Protocol.Messages.Client.Team.TeamSetLocationMessage import TeamSetLocationMessage
from Protocol.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Protocol.Messages.Client.Battle.StartGameMessage import StartGameMessage
from Protocol.Messages.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage
from Protocol.Messages.Client.Leaderboard.GetLeaderboardMessage import GetLeaderboardMessage
from Protocol.Messages.Client.Home.SetSupportedCreatorMessage import SetSupportedCreatorMessage
from Protocol.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from Protocol.Messages.Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from Protocol.Messages.Client.Clubs.CreateAllianceMessage import CreateAllianceMessage
from Protocol.Messages.Client.Clubs.AskForAllianceDataMessage import AskForAllianceDataMessage
from Protocol.Messages.Client.Clubs.ChangeAllianceSettingsMessage import ChangeAllianceSettingsMessage
from Protocol.Messages.Client.Clubs.JoinAllianceMessage import JoinAllianceMessage
from Protocol.Messages.Client.Clubs.AskForJoinableAlliancesListMessage import AskForJoinableAlliancesListMessage
from Protocol.Messages.Client.Clubs.LeaveAllianceMessage import LeaveAllianceMessage
from Protocol.Messages.Client.Clubs.SearchAlliancesMessage import SearchAlliancesMessage
from Protocol.Messages.Client.Clubs.ChatToAllianceStreamMessage import ChatToAllianceStreamMessage
from Protocol.Messages.Client.Login.ClientCryptoErrorMessage import ClientCryptoErrorMessage
from Protocol.Messages.Client.Home.PlayerStatusMessage import PlayerStatusMessage

from Protocol.Messages.Client.Clubs.ReportAllianceStreamMessage import ReportAllianceStreamMessage
from Protocol.Messages.Client.Clubs.SendAllianceMailMessage import SendAllianceMailMessage
from Protocol.Messages.Client.Clubs.ChangeAllianceMemberRoleMessage import ChangeAllianceMemberRoleMessage
from Protocol.Messages.Client.Clubs.KickAllianceMemberMessage import KickAllianceMemberMessage

packets = {

    10100: ClientHelloMessage,
    10101: LoginMessage,
    10099: ClientCryptoErrorMessage,
    10110: AnalyticsEventMessage,
    10119: ReportAllianceStreamMessage,
    14103: StartGameMessage,
    10108: KeepAliveMessage,
    10212: SetNameMessage,
    14102: EndClientTurnMessage,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: GetPlayerProfileMessage,
    14301: CreateAllianceMessage,
    14302: AskForAllianceDataMessage,
    14303: AskForJoinableAlliancesListMessage,
    14305: JoinAllianceMessage,
    14308: LeaveAllianceMessage,
    14315: ChatToAllianceStreamMessage,
    14316: ChangeAllianceSettingsMessage,
    14324: SearchAlliancesMessage,
    14306: ChangeAllianceMemberRoleMessage,
    14307: KickAllianceMemberMessage,
    14330: SendAllianceMailMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14366: PlayerStatusMessage,
    14363: TeamSetLocationMessage,
    14372: TeamToggleSettingsMessage,
    14403: GetLeaderboardMessage,
    14600: AvatarNameCheckRequestMessage,
    18686: SetSupportedCreatorMessage,

}
