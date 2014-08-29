AT^U2DIAG=0 устройство в режиме только модем
AT^U2DIAG=1 устройство в режиме модем + CD-ROM
AT^U2DIAG=255 устройство в режиме модем + CD-ROM + Card Reader
AT^U2DIAG=256 устройство в режиме модем + Card Reader

Работают следующие команды:

AT^U2DIAG=0 (девайс в режиме только модем)
AT^U2DIAG=1 (девайс в режиме модем + CD-ROM)
AT^U2DIAG=6 (девайс в режиме только сетевая карта)
AT^U2DIAG=268 для E1750 (девайс в режиме модем +
CD-ROM + Card Reader)
AT^U2DIAG=276 для E1750 (девайс в режиме сетевой
карты + CD-ROM + Card Reader)
AT^U2DIAG=256 (девайс в режиме модем + Card Reader),
можно использовать
как обычную флешку, отказавшись от установки
драйверов модема

А эта команда не работает:

AT^U2DIAG=255 (девайс в режиме модем + CD-ROM
+ Card Reader)

Источник: http://trustoff.ru/kak-vvesti-at-komandy-v-modem-cherez-hyperterminal#ixzz3BmiuelMl