import type { ReactNode } from 'react';

export interface DossierCardProps {
  /** The mono kicker above the title: the kind of document this is. */
  eyebrow?: string;
  title: string;
  /** The file reference, set in mono on the right: a case number, a date, a version. */
  reference?: string;
  /** A `<Stamp>` — the seal on the folder. */
  stamp?: ReactNode;
  children: ReactNode;
  className?: string;
}

export function DossierCard({
  eyebrow,
  title,
  reference,
  stamp,
  children,
  className,
}: DossierCardProps) {
  const aside = reference !== undefined || stamp !== undefined;
  return (
    <article className={['el-dossier', className].filter(Boolean).join(' ')}>
      <header className="el-dossier__head">
        <div className="el-dossier__headings">
          {eyebrow !== undefined && <span className="el-eyebrow">{eyebrow}</span>}
          <h3 className="el-dossier__title">{title}</h3>
        </div>
        {aside && (
          <div className="el-dossier__aside">
            {reference !== undefined && <span className="el-dossier__ref">{reference}</span>}
            {stamp}
          </div>
        )}
      </header>
      <hr className="el-dossier__rule" />
      <div className="el-dossier__body">{children}</div>
    </article>
  );
}
