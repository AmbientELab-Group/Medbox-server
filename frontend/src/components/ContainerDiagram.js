import React from "react";
import { makeStyles, useTheme } from "@material-ui/core/styles";


const useStyles = makeStyles((theme) => ({
    withShadow: {
        filter: `drop-shadow(0px 3px 1px rgba(0,0,0,0.2))`
    }
}));

const PlaceholderSvg = ({pathProps, textProps, ...rest}) => (
    <svg viewBox="-200 -200 400 400" {...rest}>
        <circle cx={0} cy={0} r="200" {...pathProps}/>
    </svg>
);

const Diagram = ({container, pathProps, textProps, ...rest}) => {
    const { capacity = 28 } = container;
    const MAX_WIDTH = 400;
    const RING_WIDTH = 60;
    const ANGLE_DELTA = 2 * Math.PI / capacity;
    const ANGLE_ORIGIN = -0.5 * Math.PI; 
    const BIG_R = MAX_WIDTH / 2 - 20;
    const SMALL_R = BIG_R - RING_WIDTH; 
    const PADDING = ANGLE_DELTA / 20;

    const points = [];
    
    for (let i = 0; i < capacity; i++) {
        points.push([
            [Math.cos(ANGLE_ORIGIN + ANGLE_DELTA * i + PADDING / 2) * SMALL_R, Math.sin(ANGLE_ORIGIN + ANGLE_DELTA * i + PADDING / 2) * SMALL_R],
            [Math.cos(ANGLE_ORIGIN + ANGLE_DELTA * (i + 1) - PADDING / 2) * SMALL_R, Math.sin(ANGLE_ORIGIN + ANGLE_DELTA * (i + 1) - PADDING / 2) * SMALL_R],
            [Math.cos(ANGLE_ORIGIN + ANGLE_DELTA * (i + 1) - PADDING / 2) * BIG_R, Math.sin(ANGLE_ORIGIN + ANGLE_DELTA * (i + 1) - PADDING / 2) * BIG_R],
            [Math.cos(ANGLE_ORIGIN + ANGLE_DELTA * i + PADDING / 2) * BIG_R, Math.sin(ANGLE_ORIGIN + ANGLE_DELTA * i + PADDING / 2) * BIG_R],
            [Math.cos(ANGLE_ORIGIN + ANGLE_DELTA * i + ANGLE_DELTA / 2 + PADDING / 2) * (SMALL_R + RING_WIDTH / 2), Math.sin(ANGLE_ORIGIN + ANGLE_DELTA * i + ANGLE_DELTA / 2 + PADDING / 2) * (SMALL_R + RING_WIDTH / 2)]
        ]);
    }
    
    return (
        <svg viewBox="-200 -200 400 400" {...rest}>
        { points.map((points, idx) => (
            <g key={`chamber-${idx}-key`}>
                <path
                    d={`M ${points[0][0]} ${points[0][1]}
                        A ${SMALL_R} ${SMALL_R} 0 0 1 ${points[1][0]} ${points[1][1]}
                        L ${points[2][0]} ${points[2][1]}
                        A ${BIG_R} ${BIG_R} 0 0 0 ${points[3][0]} ${points[3][1]}
                        Z`} 
                    stroke="transparent" 
                    strokeWidth="3"
                    id={`chamber-${idx}`}
                    {...pathProps}
                />
                <text
                    x={`${points[4][0]}`} 
                    y={`${points[4][1]}`} 
                    textAnchor="middle" 
                    fill="black"
                    id={`chamber-text-${idx}`}
                    {...textProps}
                >
                    {idx + 1}
                </text>
            </g>
        ))}
        </svg>
    );
};

const ContainerDiagram = ({container}) => {
    const theme = useTheme();
    const classes = useStyles();

    if (container) {
        return (
            <Diagram
                container={container}
                pathProps={{"fill": theme.palette.primary.light}} 
                style={{"padding": theme.spacing(3)}}
                className={classes.withShadow}
            />
        );
    } else {
        return (
            <PlaceholderSvg 
                pathProps={{"fill": theme.palette.grey[300]}} 
                style={{"padding": theme.spacing(3)}}
                className={classes.withShadow}
            />
        );
    }
}

export default ContainerDiagram;
