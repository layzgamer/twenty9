/********************************************************************************
** Form generated from reading UI file 'serverpage.ui'
**
** Created: Fri Feb 15 19:43:05 2013
**      by: Qt User Interface Compiler version 4.8.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SERVERPAGE_H
#define UI_SERVERPAGE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLineEdit>
#include <QtGui/QListView>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QTextBrowser>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QListView *Clients;
    QTextBrowser *ChatBox;
    QLineEdit *Chat;
    QVBoxLayout *verticalLayout_2;
    QPushButton *InsertBot;
    QPushButton *MoveUp;
    QPushButton *MoveDown;
    QPushButton *Remove;
    QPushButton *Start;
    QSpacerItem *verticalSpacer;
    QPushButton *Enter;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->setWindowModality(Qt::ApplicationModal);
        Dialog->resize(441, 294);
        horizontalLayout = new QHBoxLayout(Dialog);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        Clients = new QListView(Dialog);
        Clients->setObjectName(QString::fromUtf8("Clients"));

        verticalLayout->addWidget(Clients);

        ChatBox = new QTextBrowser(Dialog);
        ChatBox->setObjectName(QString::fromUtf8("ChatBox"));

        verticalLayout->addWidget(ChatBox);

        Chat = new QLineEdit(Dialog);
        Chat->setObjectName(QString::fromUtf8("Chat"));

        verticalLayout->addWidget(Chat);


        horizontalLayout->addLayout(verticalLayout);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        InsertBot = new QPushButton(Dialog);
        InsertBot->setObjectName(QString::fromUtf8("InsertBot"));

        verticalLayout_2->addWidget(InsertBot);

        MoveUp = new QPushButton(Dialog);
        MoveUp->setObjectName(QString::fromUtf8("MoveUp"));

        verticalLayout_2->addWidget(MoveUp);

        MoveDown = new QPushButton(Dialog);
        MoveDown->setObjectName(QString::fromUtf8("MoveDown"));

        verticalLayout_2->addWidget(MoveDown);

        Remove = new QPushButton(Dialog);
        Remove->setObjectName(QString::fromUtf8("Remove"));

        verticalLayout_2->addWidget(Remove);

        Start = new QPushButton(Dialog);
        Start->setObjectName(QString::fromUtf8("Start"));

        verticalLayout_2->addWidget(Start);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer);

        Enter = new QPushButton(Dialog);
        Enter->setObjectName(QString::fromUtf8("Enter"));

        verticalLayout_2->addWidget(Enter);


        horizontalLayout->addLayout(verticalLayout_2);


        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", 0, QApplication::UnicodeUTF8));
        InsertBot->setText(QApplication::translate("Dialog", "Insert Bot", 0, QApplication::UnicodeUTF8));
        MoveUp->setText(QApplication::translate("Dialog", "Move Up", 0, QApplication::UnicodeUTF8));
        MoveDown->setText(QApplication::translate("Dialog", "Move Down", 0, QApplication::UnicodeUTF8));
        Remove->setText(QApplication::translate("Dialog", "Remove", 0, QApplication::UnicodeUTF8));
        Start->setText(QApplication::translate("Dialog", "Start", 0, QApplication::UnicodeUTF8));
        Enter->setText(QApplication::translate("Dialog", "Enter", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SERVERPAGE_H
