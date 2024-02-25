import sys
import subprocess
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class SSHKeyGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('SSH Key Generator')
        self.setGeometry(100, 100, 200, 100)
        
        # Bouton pour générer la clé SSH
        self.generateButton = QPushButton('Générer Clé SSH', self)
        self.generateButton.clicked.connect(self.generateSSHKey)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.generateButton)
        self.setLayout(layout)
        
        self.show()

    def generateSSHKey(self):
        # Spécifiez le chemin où vous souhaitez sauvegarder votre clé SSH
        key_path = 'ssh_key_ed25519'
        try:
            # Générer la clé SSH sans commentaire
            subprocess.run(['ssh-keygen', '-t', 'ed25519', '-N', '', '-f', key_path], shell=True, check=True)
            # Lire la clé publique générée
            with open(f'{key_path}.pub', 'r') as file:
                ssh_key = file.read()
                # Copier la clé dans le presse-papiers
                pyperclip.copy(ssh_key)
                QMessageBox.information(self, 'Succès', 'Votre clé est dans le presse-papier, vous pouvez la coller dans GitLab.')
        except Exception as e:
            QMessageBox.critical(self, 'Erreur', f'Une erreur est survenue lors de la génération de la clé SSH : {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SSHKeyGenerator()
    sys.exit(app.exec_())
