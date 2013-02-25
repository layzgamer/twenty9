/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created: Fri Feb 15 19:43:05 2013
**      by: Qt User Interface Compiler version 4.8.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QMainWindow>
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *SaveGame;
    QAction *LoadGame;
    QAction *Exit;
    QAction *Help;
    QAction *Preferences;
    QAction *JoinGame;
    QAction *SinglePlayer;
    QAction *CreateGame;
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QGroupBox *opponentScore;
    QPushButton *OpponentScoreCardFront;
    QPushButton *OpponentScoreCardBack;
    QGroupBox *SelfScore;
    QPushButton *SelfScoreCardFront;
    QPushButton *SelfScoreCardBack;
    QGroupBox *emptyBox2;
    QGroupBox *LeftHand;
    QPushButton *LeftCard;
    QGroupBox *emptyBox1;
    QPushButton *TopCard_2;
    QGroupBox *Pit;
    QPushButton *LeftPit;
    QPushButton *TopPit;
    QPushButton *RightPit;
    QPushButton *BottomPit;
    QGroupBox *RightHand;
    QPushButton *RightCard;
    QGroupBox *BottomHand;
    QPushButton *BottomCard;
    QGroupBox *TopHand;
    QPushButton *TopCard;
    QMenuBar *menuBar;
    QMenu *GameMenu;
    QMenu *NewGameMenu;
    QMenu *HelpMenu;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(800, 694);
        MainWindow->setStyleSheet(QString::fromUtf8("background-image:url(:/backgrounds/backgrounds/background.jpg)"));
        SaveGame = new QAction(MainWindow);
        SaveGame->setObjectName(QString::fromUtf8("SaveGame"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/icons/save.png"), QSize(), QIcon::Normal, QIcon::Off);
        SaveGame->setIcon(icon);
        QFont font;
        font.setFamily(QString::fromUtf8("Century Schoolbook L"));
        font.setBold(true);
        font.setWeight(75);
        SaveGame->setFont(font);
        LoadGame = new QAction(MainWindow);
        LoadGame->setObjectName(QString::fromUtf8("LoadGame"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/icons/open.png"), QSize(), QIcon::Normal, QIcon::Off);
        LoadGame->setIcon(icon1);
        LoadGame->setFont(font);
        Exit = new QAction(MainWindow);
        Exit->setObjectName(QString::fromUtf8("Exit"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/icons/exit.png"), QSize(), QIcon::Normal, QIcon::Off);
        Exit->setIcon(icon2);
        Exit->setFont(font);
        Help = new QAction(MainWindow);
        Help->setObjectName(QString::fromUtf8("Help"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/icons/help.png"), QSize(), QIcon::Normal, QIcon::Off);
        Help->setIcon(icon3);
        Help->setFont(font);
        Preferences = new QAction(MainWindow);
        Preferences->setObjectName(QString::fromUtf8("Preferences"));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/icons/settings.png"), QSize(), QIcon::Normal, QIcon::Off);
        Preferences->setIcon(icon4);
        Preferences->setFont(font);
        JoinGame = new QAction(MainWindow);
        JoinGame->setObjectName(QString::fromUtf8("JoinGame"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/icons/join.png"), QSize(), QIcon::Normal, QIcon::Off);
        JoinGame->setIcon(icon5);
        JoinGame->setFont(font);
        SinglePlayer = new QAction(MainWindow);
        SinglePlayer->setObjectName(QString::fromUtf8("SinglePlayer"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icons/icons/user.png"), QSize(), QIcon::Normal, QIcon::Off);
        SinglePlayer->setIcon(icon6);
        SinglePlayer->setFont(font);
        CreateGame = new QAction(MainWindow);
        CreateGame->setObjectName(QString::fromUtf8("CreateGame"));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/icons/icons/create.png"), QSize(), QIcon::Normal, QIcon::Off);
        CreateGame->setIcon(icon7);
        CreateGame->setFont(font);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        centralWidget->setMinimumSize(QSize(800, 620));
        centralWidget->setAutoFillBackground(false);
        centralWidget->setStyleSheet(QString::fromUtf8("background:transparent"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        opponentScore = new QGroupBox(centralWidget);
        opponentScore->setObjectName(QString::fromUtf8("opponentScore"));
        OpponentScoreCardFront = new QPushButton(opponentScore);
        OpponentScoreCardFront->setObjectName(QString::fromUtf8("OpponentScoreCardFront"));
        OpponentScoreCardFront->setGeometry(QRect(40, 0, 86, 124));
        OpponentScoreCardFront->setMinimumSize(QSize(86, 124));
        OpponentScoreCardBack = new QPushButton(opponentScore);
        OpponentScoreCardBack->setObjectName(QString::fromUtf8("OpponentScoreCardBack"));
        OpponentScoreCardBack->setGeometry(QRect(70, 0, 86, 124));
        OpponentScoreCardBack->setMinimumSize(QSize(86, 124));

        gridLayout->addWidget(opponentScore, 0, 0, 1, 1);

        SelfScore = new QGroupBox(centralWidget);
        SelfScore->setObjectName(QString::fromUtf8("SelfScore"));
        SelfScoreCardFront = new QPushButton(SelfScore);
        SelfScoreCardFront->setObjectName(QString::fromUtf8("SelfScoreCardFront"));
        SelfScoreCardFront->setGeometry(QRect(50, 10, 86, 124));
        SelfScoreCardFront->setMinimumSize(QSize(86, 124));
        SelfScoreCardBack = new QPushButton(SelfScore);
        SelfScoreCardBack->setObjectName(QString::fromUtf8("SelfScoreCardBack"));
        SelfScoreCardBack->setGeometry(QRect(80, 10, 86, 124));
        SelfScoreCardBack->setMinimumSize(QSize(86, 124));

        gridLayout->addWidget(SelfScore, 3, 2, 1, 1);

        emptyBox2 = new QGroupBox(centralWidget);
        emptyBox2->setObjectName(QString::fromUtf8("emptyBox2"));
        emptyBox2->setFlat(true);

        gridLayout->addWidget(emptyBox2, 3, 0, 1, 1);

        LeftHand = new QGroupBox(centralWidget);
        LeftHand->setObjectName(QString::fromUtf8("LeftHand"));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Century Schoolbook L"));
        font1.setPointSize(12);
        font1.setItalic(true);
        LeftHand->setFont(font1);
        LeftCard = new QPushButton(LeftHand);
        LeftCard->setObjectName(QString::fromUtf8("LeftCard"));
        LeftCard->setGeometry(QRect(80, 30, 86, 124));
        LeftCard->setMinimumSize(QSize(86, 124));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/backs/backs/back.png"), QSize(), QIcon::Normal, QIcon::Off);
        LeftCard->setIcon(icon8);
        LeftCard->setIconSize(QSize(81, 119));

        gridLayout->addWidget(LeftHand, 1, 0, 2, 1);

        emptyBox1 = new QGroupBox(centralWidget);
        emptyBox1->setObjectName(QString::fromUtf8("emptyBox1"));
        emptyBox1->setFlat(true);
        TopCard_2 = new QPushButton(emptyBox1);
        TopCard_2->setObjectName(QString::fromUtf8("TopCard_2"));
        TopCard_2->setGeometry(QRect(90, 10, 86, 124));
        TopCard_2->setMinimumSize(QSize(86, 124));
        TopCard_2->setIcon(icon8);
        TopCard_2->setIconSize(QSize(81, 119));

        gridLayout->addWidget(emptyBox1, 0, 2, 1, 1);

        Pit = new QGroupBox(centralWidget);
        Pit->setObjectName(QString::fromUtf8("Pit"));
        LeftPit = new QPushButton(Pit);
        LeftPit->setObjectName(QString::fromUtf8("LeftPit"));
        LeftPit->setGeometry(QRect(50, 70, 86, 124));
        LeftPit->setMinimumSize(QSize(86, 124));
        TopPit = new QPushButton(Pit);
        TopPit->setObjectName(QString::fromUtf8("TopPit"));
        TopPit->setGeometry(QRect(90, 40, 86, 124));
        TopPit->setMinimumSize(QSize(86, 124));
        RightPit = new QPushButton(Pit);
        RightPit->setObjectName(QString::fromUtf8("RightPit"));
        RightPit->setGeometry(QRect(140, 70, 86, 124));
        RightPit->setMinimumSize(QSize(86, 124));
        BottomPit = new QPushButton(Pit);
        BottomPit->setObjectName(QString::fromUtf8("BottomPit"));
        BottomPit->setGeometry(QRect(90, 100, 86, 124));
        BottomPit->setMinimumSize(QSize(86, 124));

        gridLayout->addWidget(Pit, 1, 1, 2, 1);

        RightHand = new QGroupBox(centralWidget);
        RightHand->setObjectName(QString::fromUtf8("RightHand"));
        RightHand->setMinimumSize(QSize(0, 0));
        RightHand->setFont(font1);
        RightCard = new QPushButton(RightHand);
        RightCard->setObjectName(QString::fromUtf8("RightCard"));
        RightCard->setGeometry(QRect(90, 30, 86, 124));
        RightCard->setMinimumSize(QSize(86, 124));
        RightCard->setIcon(icon8);
        RightCard->setIconSize(QSize(81, 119));

        gridLayout->addWidget(RightHand, 1, 2, 2, 1);

        BottomHand = new QGroupBox(centralWidget);
        BottomHand->setObjectName(QString::fromUtf8("BottomHand"));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Century Schoolbook L"));
        font2.setPointSize(12);
        font2.setBold(true);
        font2.setItalic(true);
        font2.setWeight(75);
        BottomHand->setFont(font2);
        BottomHand->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        BottomCard = new QPushButton(BottomHand);
        BottomCard->setObjectName(QString::fromUtf8("BottomCard"));
        BottomCard->setGeometry(QRect(10, 30, 86, 124));
        BottomCard->setMinimumSize(QSize(86, 124));
        BottomCard->setCursor(QCursor(Qt::PointingHandCursor));

        gridLayout->addWidget(BottomHand, 3, 1, 1, 1);

        TopHand = new QGroupBox(centralWidget);
        TopHand->setObjectName(QString::fromUtf8("TopHand"));
        TopHand->setFont(font1);
        TopCard = new QPushButton(TopHand);
        TopCard->setObjectName(QString::fromUtf8("TopCard"));
        TopCard->setGeometry(QRect(0, 30, 86, 124));
        TopCard->setMinimumSize(QSize(86, 124));
        TopCard->setIcon(icon8);
        TopCard->setIconSize(QSize(81, 119));

        gridLayout->addWidget(TopHand, 0, 1, 1, 1);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 800, 24));
        menuBar->setFont(font);
        GameMenu = new QMenu(menuBar);
        GameMenu->setObjectName(QString::fromUtf8("GameMenu"));
        GameMenu->setFont(font);
        NewGameMenu = new QMenu(GameMenu);
        NewGameMenu->setObjectName(QString::fromUtf8("NewGameMenu"));
        NewGameMenu->setFont(font);
        HelpMenu = new QMenu(menuBar);
        HelpMenu->setObjectName(QString::fromUtf8("HelpMenu"));
        HelpMenu->setFont(font);
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        mainToolBar->setFont(font);
        mainToolBar->setStyleSheet(QString::fromUtf8("background:transparent"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        statusBar->setStyleSheet(QString::fromUtf8("background:transparent"));
        MainWindow->setStatusBar(statusBar);
        QWidget::setTabOrder(BottomCard, OpponentScoreCardFront);
        QWidget::setTabOrder(OpponentScoreCardFront, OpponentScoreCardBack);
        QWidget::setTabOrder(OpponentScoreCardBack, TopCard);
        QWidget::setTabOrder(TopCard, LeftPit);
        QWidget::setTabOrder(LeftPit, TopPit);
        QWidget::setTabOrder(TopPit, RightPit);
        QWidget::setTabOrder(RightPit, BottomPit);
        QWidget::setTabOrder(BottomPit, RightCard);
        QWidget::setTabOrder(RightCard, LeftCard);
        QWidget::setTabOrder(LeftCard, SelfScoreCardFront);
        QWidget::setTabOrder(SelfScoreCardFront, SelfScoreCardBack);

        menuBar->addAction(GameMenu->menuAction());
        menuBar->addAction(HelpMenu->menuAction());
        GameMenu->addAction(NewGameMenu->menuAction());
        GameMenu->addAction(SaveGame);
        GameMenu->addAction(LoadGame);
        GameMenu->addSeparator();
        GameMenu->addAction(Preferences);
        GameMenu->addSeparator();
        GameMenu->addAction(Exit);
        NewGameMenu->addAction(CreateGame);
        NewGameMenu->addAction(JoinGame);
        NewGameMenu->addAction(SinglePlayer);
        HelpMenu->addAction(Help);
        mainToolBar->addAction(CreateGame);
        mainToolBar->addAction(JoinGame);
        mainToolBar->addAction(SinglePlayer);
        mainToolBar->addSeparator();
        mainToolBar->addAction(SaveGame);
        mainToolBar->addAction(LoadGame);
        mainToolBar->addSeparator();
        mainToolBar->addAction(Preferences);
        mainToolBar->addAction(Help);
        mainToolBar->addSeparator();
        mainToolBar->addAction(Exit);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "twenty9", 0, QApplication::UnicodeUTF8));
        SaveGame->setText(QApplication::translate("MainWindow", "Save Game", 0, QApplication::UnicodeUTF8));
        SaveGame->setShortcut(QApplication::translate("MainWindow", "Ctrl+S", 0, QApplication::UnicodeUTF8));
        LoadGame->setText(QApplication::translate("MainWindow", "Load Game", 0, QApplication::UnicodeUTF8));
        LoadGame->setShortcut(QApplication::translate("MainWindow", "Ctrl+O", 0, QApplication::UnicodeUTF8));
        Exit->setText(QApplication::translate("MainWindow", "Exit", 0, QApplication::UnicodeUTF8));
        Help->setText(QApplication::translate("MainWindow", "Open Readme", 0, QApplication::UnicodeUTF8));
        Help->setShortcut(QApplication::translate("MainWindow", "Ctrl+H", 0, QApplication::UnicodeUTF8));
        Preferences->setText(QApplication::translate("MainWindow", "Preferences", 0, QApplication::UnicodeUTF8));
        Preferences->setShortcut(QApplication::translate("MainWindow", "Ctrl+P", 0, QApplication::UnicodeUTF8));
        JoinGame->setText(QApplication::translate("MainWindow", "Join Game", 0, QApplication::UnicodeUTF8));
        JoinGame->setShortcut(QApplication::translate("MainWindow", "Ctrl+J", 0, QApplication::UnicodeUTF8));
        SinglePlayer->setText(QApplication::translate("MainWindow", "Single Player", 0, QApplication::UnicodeUTF8));
        SinglePlayer->setShortcut(QApplication::translate("MainWindow", "Ctrl+B", 0, QApplication::UnicodeUTF8));
        CreateGame->setText(QApplication::translate("MainWindow", "Create Game", 0, QApplication::UnicodeUTF8));
        CreateGame->setShortcut(QApplication::translate("MainWindow", "Ctrl+N", 0, QApplication::UnicodeUTF8));
        opponentScore->setTitle(QString());
        OpponentScoreCardFront->setText(QString());
        OpponentScoreCardBack->setText(QString());
        SelfScore->setTitle(QString());
        SelfScoreCardFront->setText(QString());
        SelfScoreCardBack->setText(QString());
        emptyBox2->setTitle(QString());
        LeftHand->setTitle(QApplication::translate("MainWindow", "PlayerName", 0, QApplication::UnicodeUTF8));
        LeftCard->setText(QString());
        emptyBox1->setTitle(QString());
        TopCard_2->setText(QString());
        Pit->setTitle(QString());
        LeftPit->setText(QString());
        TopPit->setText(QString());
        RightPit->setText(QString());
        BottomPit->setText(QString());
        RightHand->setTitle(QApplication::translate("MainWindow", "PlayerName", 0, QApplication::UnicodeUTF8));
        RightCard->setText(QString());
        BottomHand->setTitle(QApplication::translate("MainWindow", "PlayerName", 0, QApplication::UnicodeUTF8));
        TopHand->setTitle(QApplication::translate("MainWindow", "PlayerName", 0, QApplication::UnicodeUTF8));
        TopCard->setText(QString());
        GameMenu->setTitle(QApplication::translate("MainWindow", "Game", 0, QApplication::UnicodeUTF8));
        NewGameMenu->setTitle(QApplication::translate("MainWindow", "New Game", 0, QApplication::UnicodeUTF8));
        HelpMenu->setTitle(QApplication::translate("MainWindow", "Help", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
