from db import db
from datetime import datetime

# Tabela de Usuários
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)  # Nome do usuário
    username = db.Column(db.String(80), unique=True, nullable=False)  # Login único
    password = db.Column(db.String(128), nullable=False)  # Senha (em produção, use hash!)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  # Se é admin
    is_employee = db.Column(db.Boolean, default=True, nullable=False)  # Se é funcionário
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Data de criação

    def __repr__(self):
        return f'<User {self.username}>'

# Tabela de Horários Padrão dos Funcionários (cadastrado pelo admin)
class EmployeeSchedule(db.Model):
    __tablename__ = 'employee_schedules'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # FK para User
    entry_time = db.Column(db.Time, nullable=False)  # Horário de entrada padrão
    lunch_start = db.Column(db.Time, nullable=True)  # Início do almoço (agora pode ser nulo)
    lunch_end = db.Column(db.Time, nullable=True)    # Fim do almoço (agora pode ser nulo)
    exit_time = db.Column(db.Time, nullable=False)    # Saída

    user = db.relationship('User', backref='schedule')

    def __repr__(self):
        return f'<EmployeeSchedule {self.user_id}>'

# Tabela de Registros de Ponto (batidas diárias)
class TimeRecord(db.Model):
    __tablename__ = 'time_records'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # FK para User
    date = db.Column(db.Date, nullable=False)  # Data do registro
    entry_time = db.Column(db.Time)            # Horário de entrada batido
    lunch_start = db.Column(db.Time)           # Início do almoço batido
    lunch_end = db.Column(db.Time)             # Fim do almoço batido
    exit_time = db.Column(db.Time)             # Saída batida
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='time_records')

    def __repr__(self):
        return f'<TimeRecord {self.user_id} {self.date}>'

# Tabela de Justificativas de Ausência/Atraso
class Justification(db.Model):
    __tablename__ = 'justifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # FK para User
    date = db.Column(db.Date, nullable=False)  # Data da justificativa
    reason = db.Column(db.String(255), nullable=False)  # Motivo
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    reviewed_at = db.Column(db.DateTime)

    user = db.relationship('User', backref='justifications')

    def __repr__(self):
        return f'<Justification {self.user_id} {self.date} {self.status}>'


