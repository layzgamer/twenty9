/********************************************************************************
** Form generated from reading UI file 'joingame.ui'
**
** Created: Fri Feb 15 19:43:05 2013
**      by: Qt User Interface Compiler version 4.8.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_JOINGAME_H
#define UI_JOINGAME_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QFormLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout;
    QFormLayout *formLayout;
    QLabel *NameLabel;
    QLineEdit *Name;
    QLabel *ServerLabel;
    QLineEdit *Server;
    QLabel *PortLabel;
    QLineEdit *Port;
    QPushButton *Join;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->setWindowModality(Qt::ApplicationModal);
        Dialog->resize(268, 121);
        verticalLayout = new QVBoxLayout(Dialog);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        formLayout = new QFormLayout();
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        NameLabel = new QLabel(Dialog);
        NameLabel->setObjectName(QString::fromUtf8("NameLabel"));

        formLayout->setWidget(0, QFormLayout::LabelRole, NameLabel);

        Name = new QLineEdit(Dialog);
        Name->setObjectName(QString::fromUtf8("Name"));

        formLayout->setWidget(0, QFormLayout::FieldRole, Name);

        ServerLabel = new QLabel(Dialog);
        ServerLabel->setObjectName(QString::fromUtf8("ServerLabel"));

        formLayout->setWidget(1, QFormLayout::LabelRole, ServerLabel);

        Server = new QLineEdit(Dialog);
        Server->setObjectName(QString::fromUtf8("Server"));

        formLayout->setWidget(1, QFormLayout::FieldRole, Server);

        PortLabel = new QLabel(Dialog);
        PortLabel->setObjectName(QString::fromUtf8("PortLabel"));

        formLayout->setWidget(2, QFormLayout::LabelRole, PortLabel);

        Port = new QLineEdit(Dialog);
        Port->setObjectName(QString::fromUtf8("Port"));

        formLayout->setWidget(2, QFormLayout::FieldRole, Port);


        verticalLayout->addLayout(formLayout);

        Join = new QPushButton(Dialog);
        Join->setObjectName(QString::fromUtf8("Join"));

        verticalLayout->addWidget(Join);


        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", 0, QApplication::UnicodeUTF8));
        NameLabel->setText(QApplication::translate("Dialog", "Name", 0, QApplication::UnicodeUTF8));
        ServerLabel->setText(QApplication::translate("Dialog", "Server", 0, QApplication::UnicodeUTF8));
        PortLabel->setText(QApplication::translate("Dialog", "Port", 0, QApplication::UnicodeUTF8));
        Join->setText(QApplication::translate("Dialog", "Join", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_JOINGAME_H
