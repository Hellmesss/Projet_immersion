#include <iostream>
#include <string>
#include <cstdio> // input / output / SEEK_END
#include <cstring> // c_str()
#include <cstdlib> // errno
#include <vector>
#include <fstream>

using namespace std;

int main() {
	system("chcp 1252");
	// Variable
	string path;
	int fileSize;
	FILE* pFile = NULL; // Pointeur donc on initialise à NULL
	errno_t err;

	// Ouverture du fichier
	do {
		cout << "Entrer le nom de l'image(acapulcoA11.bmp): ";
		getline(cin, path);

		err = fopen_s(&pFile, path.c_str(), "r");

	} while (err != 0); // Si le fichier ne s'ouvre pas, redemander le path

	// Get taille fichier
	fseek(pFile, 0, SEEK_END); // Position à la fin
	fileSize = ftell(pFile); // Get taille fichier
	rewind(pFile); // Remet la position au debut du fichier

		// Structure file
	unsigned char* corp = new unsigned char[fileSize]; // Char dynamique
	vector<unsigned char> dataImg;
	dataImg.reserve(fileSize);


	// Lecture du fichier
	fread(corp, sizeof(unsigned char), fileSize, pFile);

	// get bit de poid faible de chaque char
	for (int i = 0; i < fileSize; i++) {
		if (corp[i] % 2 == 1) { // Check si carac est impair / pair 
			dataImg.push_back(true); // Push back 1 dans le vector dataImg si carac est impair
		}
		else {
			dataImg.push_back(false); // Push back 0 dans le vector dataImg si carac est pair
		}
	}

	// fermeture du fichier.
	fclose(pFile);

	// Demander l'offset pour bien commencer au bon bit [0,0,0,0,0,0,0,0]
	int offset;
	cout << "\nPour aligner bien correctement les octets, il faut entrer un offset. (Entrer 2 pour l'image acapulco)\n";
	cout << "Entrer une valeur pour l'offset (0 à 8): ";
	cin >> offset;

	dataImg.erase(dataImg.begin(), dataImg.begin() + offset); // application de l'offset ex: Si offset = 2 on supprime les 2 premières valeurs de dataImg


	/* Regroupe les bits en octet.
	*
	* /!\ Dans dataImg, true représente [0,0,0,0,0,0,0,1] et false [0,0,0,0,0,0,0,0]
	* donc on prend les 8 premières valeurs de dataImg et on les "regroupe".
	*
	* Exemple:
	* 8 valeur de dataImg => [0,0,0,0,0,0,0,1] [0,0,0,0,0,0,0,0] [0,0,0,0,0,0,0,0] [0,0,0,0,0,0,0,1]
	*                        [0,0,0,0,0,0,0,1] [0,0,0,0,0,0,0,1] [0,0,0,0,0,0,0,1] [0,0,0,0,0,0,0,0]
	*
	* On cherchera donc a avoir => = [1,0,0,1,1,1,1,0]
	* On fais donc un ET logique.
	* */

	// ET logique
	vector<unsigned char> listOctet; // vector où seront stocker les octets regroupés
	int j = 0; // Counter qu'on augmentera de 8 à chaque fin de traitement d'octet pour traiter l'octet suivant
	while (j < dataImg.size() - 7) {
		unsigned char octet = 0; // On remet unsigned char octet a 0 pour traiter un nouveau octet, si on le place pas dans la boucle, la valeur de unsigned char octet, gardera la valeur de l'ancien octet. Donc on aurait uniquement le 1er octet de juste et la suite serait fausse.
		for (int i = 7; 0 <= i; i--) { // 7 car on compte le 0
			unsigned char bitOne = 1; // [1,1,1,1,1,1,1,1]
			if (dataImg[i + j] == true) { // si true dans dataImg
				bitOne <<= (7 - i); // operator bitwise 
				octet |= bitOne; // octet = octet | bitOne
			}
		}
		listOctet.push_back(octet); // Push back l'octet final dans le vector
		j += 8;
	}

	cout << "\n\nLe message est:\n\n";
	for (int i = 19; i <= 219; i++) // 19 car le message commence aux 19e octet et 219 car il se finit aux 219 octet
		cout << listOctet[i];

	cout << "\n\nUn fichier audio a était crée sur le repertoire courant du programme..." << endl;

	FILE* audioFile = NULL;
	fopen_s(&audioFile, "audio.m4a", "wb"); // ici on met bien w et non pas r comme vue plus haut, car on ecrit dans le fichier, on ne le lit pas.
	fwrite(&listOctet[220], sizeof(char), listOctet.size(), audioFile); // on write tout dans le fichier à partir du 220e octet (après la fin du message)

	delete[](corp); // ne pas oublier le unsigned char octet dynamique
	return(0);
}
