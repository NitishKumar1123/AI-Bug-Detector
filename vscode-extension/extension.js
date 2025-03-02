// vscode-extension/extension.js/
const vscode = require("vscode");
const axios = require("axios");

function activate(context) {
    let disposable = vscode.commands.registerCommand("extension.detectBug", async function () {
        let editor = vscode.window.activeTextEditor;
        if (!editor) return;

        let code = editor.document.getText();

        try {
            let response = await axios.post("http://localhost:5000/upload", 
                { code: code },
                { headers: { "Content-Type": "multipart/form-data" } }
            );
            
            vscode.window.showInformationMessage(`Bug Detected: ${response.data.bug_type}`);
        } catch (error) {
            vscode.window.showErrorMessage("Error detecting bug.");
        }
    });

    context.subscriptions.push(disposable);
}

exports.activate = activate;
