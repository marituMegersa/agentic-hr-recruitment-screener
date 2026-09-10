from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.hr_recruitment_screener.models import AgenticHrRecruitmentScreenerSession, AgenticHrRecruitmentScreenerItem
from app.domain.hr_recruitment_screener.schemas import AgenticHrRecruitmentScreenerSessionCreate, AgenticHrRecruitmentScreenerItemCreate

class AgenticHrRecruitmentScreenerService:
    @staticmethod
    def create_session(db: Session, data: AgenticHrRecruitmentScreenerSessionCreate) -> AgenticHrRecruitmentScreenerSession:
        db_obj = AgenticHrRecruitmentScreenerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticHrRecruitmentScreenerSession:
        return db.query(AgenticHrRecruitmentScreenerSession).filter(AgenticHrRecruitmentScreenerSession.id == session_id).first()
