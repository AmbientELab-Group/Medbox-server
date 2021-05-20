import styled from "styled-components";
import MuiAvatar from "@material-ui/core/Avatar";

const Avatar = styled(MuiAvatar)`
    margin: ${({ theme }) => theme.spacing(1)};
    background: ${({ theme }) => theme.palette.primary.gradient};
`;

export default Avatar;
