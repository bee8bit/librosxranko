import { Sequelize, DataTypes, Model } from 'sequelize';

class User extends Model {
    declare id: number;
    declare firstName: string;
    declare lastName: string;
}

User.init({
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true
    },
    firstName: {
        type: DataTypes.STRING
    },
    lastName: {
        type: DataTypes.STRING,
        allowNull: false
    }
},
{
    sequelize,
    modelName: 'Benutzer'
});