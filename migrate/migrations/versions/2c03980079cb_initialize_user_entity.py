"""Initialize User Entity

Revision ID: 2c03980079cb
Revises: 
Create Date: 2021-12-27 16:28:07.875783

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column


# revision identifiers, used by Alembic.
revision = '2c03980079cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    users_table = op.create_table('users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(30), unique=True, nullable=False),
        sa.Column('docker_image', sa.String(4096), nullable=False),
        sa.Column('version', sa.String(30), nullable=False),
        sa.Column('gpu_device', sa.String(10), nullable=False),
        sa.Column('port_range', sa.String(20), nullable=False))
    
    op.bulk_insert(users_table,
        [
            {'id': 1, 'username': 'innoacad01', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '0:0', 'port_range': '10100-10110'},
            {'id': 2, 'username': 'innoacad02', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '0:1', 'port_range': '10200-10210'},
            {'id': 3, 'username': 'innoacad03', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '0:2', 'port_range': '10300-10310'},
            {'id': 4, 'username': 'innoacad04', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '0:3', 'port_range': '10400-10410'},
            {'id': 5, 'username': 'innoacad05', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '0:4', 'port_range': '10500-10510'},
            {'id': 6, 'username': 'innoacad06', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '0:5', 'port_range': '10600-10610'},
            {'id': 7, 'username': 'innoacad07', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '0:6', 'port_range': '10700-10710'},
            {'id': 8, 'username': 'innoacad08', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '1:0', 'port_range': '10800-10810'},
            {'id': 9, 'username': 'innoacad09', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '1:1', 'port_range': '10900-10910'},
            {'id': 10, 'username': 'innoacad10', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '1:2', 'port_range': '11000-11010'},
            {'id': 11, 'username': 'innoacad11', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '1:3', 'port_range': '11100-11110'},
            {'id': 12, 'username': 'innoacad12', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '1:4', 'port_range': '11200-11210'},
            {'id': 13, 'username': 'innoacad13', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '1:5', 'port_range': '11300-11310'},
            {'id': 14, 'username': 'innoacad14', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '1:6', 'port_range': '11400-11410'},
            {'id': 15, 'username': 'innoacad15', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '2:0', 'port_range': '11500-11510'},
            {'id': 16, 'username': 'innoacad16', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '2:1', 'port_range': '11600-11610'},
            {'id': 17, 'username': 'innoacad17', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '2:2', 'port_range': '11700-11710'},
            {'id': 18, 'username': 'innoacad18', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '2:3', 'port_range': '11800-11810'},
            {'id': 19, 'username': 'innoacad19', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '2:4', 'port_range': '11900-11910'},
            {'id': 20, 'username': 'innoacad20', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '2:5', 'port_range': '12000-12010'},
            {'id': 21, 'username': 'innoacad21', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '2:6', 'port_range': '12100-12110'},
            {'id': 22, 'username': 'innoacad22', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '3:0', 'port_range': '12200-12210'},
            {'id': 23, 'username': 'innoacad23', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '3:1', 'port_range': '12300-12310'},
            {'id': 24, 'username': 'innoacad24', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '3:2', 'port_range': '12400-12410'},
            {'id': 25, 'username': 'innoacad25', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '3:3', 'port_range': '12500-12510'},
            {'id': 26, 'username': 'innoacad26', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '3:4', 'port_range': '12600-12610'},
            {'id': 27, 'username': 'innoacad27', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '3:5', 'port_range': '12700-12710'},
            {'id': 28, 'username': 'innoacad28', 'docker_image': 'nvidia/cuda:11.1-base', 'version': '1.0.0', 'gpu_device': '3:6', 'port_range': '12800-12810'},
        ])
    pass


def downgrade():
    op.drop_table('users')
    pass
