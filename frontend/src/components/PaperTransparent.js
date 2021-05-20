import styled from "styled-components";
import MuiPaper from "@material-ui/core/Paper";

const PaperTransparent = styled(MuiPaper)`
    background: ${({ theme }) => theme.palette.background.transparentPaper};
    background: ${({ theme }) => theme.palette.background.transparentPaperGradient};
`;

export default PaperTransparent;
