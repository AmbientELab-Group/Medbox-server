import React, { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import { useTranslation } from "react-i18next";
import { Typography } from "@material-ui/core";
import axios from "axios";

const SignUpModal = ({ open, handleClose }) => {
    const { t } = useTranslation("account");
    const [email, setEmail] = useState("");
    const [isInvalid, setInvalid] = useState(false);

    const handleChange = (event) => {
        setInvalid(false);
        setEmail(event.target.value);
    };

    const handleAccept = () => {
        const emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;
        if (emailRegex.test(email)) {
            axios
                .post(
                    "https://us-central1-flowing-access-311114.cloudfunctions.net/subscriptions",
                    {
                        email,
                    }
                )
                .catch((err) => console.log(err.response));
            handleClose();
        } else {
            setInvalid(true);
        }
    };

    return (
        <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="form-dialog-title"
        >
            <DialogTitle id="form-dialog-title" disableTypography>
                <Typography variant="h3">{t("modal.title")}</Typography>
            </DialogTitle>
            <DialogContent>
                <DialogContentText>{t("modal.message")}</DialogContentText>
                <TextField
                    autoFocus
                    margin="dense"
                    id="name"
                    label={t("formFields.email")}
                    type="email"
                    fullWidth
                    value={email}
                    onChange={handleChange}
                    error={isInvalid}
                    helperText={
                        isInvalid
                            ? t("formValidation.invalid", {
                                  field: t("formFields.email"),
                              })
                            : ""
                    }
                />
            </DialogContent>
            <DialogActions>
                <Button onClick={handleAccept} color="primary">
                    {t("modal.accept")}
                </Button>
                <Button onClick={handleClose} color="primary">
                    {t("modal.cancel")}
                </Button>
            </DialogActions>
        </Dialog>
    );
};

export default SignUpModal;
