# automaticke_kopirovani
Skript slouží k automatickému vkládání sériových čísel Thermomixů do protokolu sériových čísel do Logi.

## Návod k použití
### Před prvním spuštěním
Po stažení programu byste měli mít ve složce s programem následující položky:
- `automaticke_kopirovani.exe` je samotný program,
- složka `src` (NEMAZAT, NEZBYTNÁ PRO SPRÁVNÉ FUNGOVÁNÍ PROGRAMU),
- složka `input`, ve které se nachází 2 soubory, `test1.txt` a `test2.txt`. Tyto soubory slouží čistě pro testovací účely, neplánujete-li provádět testovací pokusy, rovnou je smažte.

Nic jiného není pro fungování programu potřeba.

Ve složce `src` je umístěn modul, který se stará o zpracovávání dat. Jeho odstranění by způsobilo chybu v chodu programu a nebyl by použitelný.

Ze složky `input` bere program všechna data. Při spuštění program přečte všechny soubory v této složce a vyextrahuje všechna SN, čísla dokumentů i počty jednotek. Program sám podle formátu čísla rozpozná, o jaké číslo se jedná. Není tedy nutné data nijak upravovat a nezáleží na tom, zda jsou všechna v jedno souboru či jsou rozdělena do více souborů.
> V případě, že dojde ke změně ze strany klienta a změní se formát SN či jiného čísla, kontaktuje prosím vývojáře (kontakt na konci manuálu), nebo osobu, která je dosatečně zdatná na to, aby změnu do programu implementovala. 

### Příprava ke spuštění
Než je program možné použít, je potřeba dostat do složky `input` všechna sériová čísla z příjmového listu. Doporučuji následující postup:
1. Stáhněte si do telefonu čtečku QR kódů, nejlépe takovou, která podporuje sdílení přímo na váš e-mail.
2. Smažte ze složky `input` všechny soubory, které nechcete zpracovávat.
3. Připravte si všechny doklady, které obsahují SN přijatých Thermomixů. Pro každý list opakujte následující postup. Kroky i a ii můžete nejprve provést společně pro všechny listy a až pak se přesunout ke kroku iii.
    1. Vaší QR čtečkou v telefonu naskenujte QR kód na listu. Měli byste vidět seznam obsahující číslo listu, počet jednotek na paletě a SN přo každou jednotku.
    2. Vyberte v aplikaci možnost *Sdílet* a v seznamu možností najděte sdílení na e-mail. Zadejte e-mail, ke kterému máte přístup na vašem pracovním PC.
    3. Obsah celého e-mailu zkopírujte do souboru umístěného ve složce `input`.

Po přesunutí všech SN do počítače si připravíme program Logi.

1. Založte novou příjemku a vyplňte všechny potřebné údaje.
2. Uložte a zavřete okno příjemky.
3. Klikněte pravým tlačítkem myši na příjemku a vyberte možnost ***Nástroje $\rarr$ Sériová čísla.***
4. Klikněte dovnitř prázdné tabulky jako kdybyste se chystali čísla psát manuálně, ale nic dovnitř nepište.

Nyní máme Logi připravené pro vkládání SN. Pokud omylem okno *Sériová čísla * zavřete, otevřete si ho znovu a klikněte do prázdné tabulky.

Můžete spustit program (`automaticke_kopirovani.exe`) a řiďte se jeho instrukcemi.