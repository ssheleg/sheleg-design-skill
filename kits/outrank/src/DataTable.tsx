import type { ReactNode } from 'react';

export interface DataTableColumn {
  key: string;
  label: string;
  /** Right-align and tabular-figure this column. */
  numeric?: boolean;
}

export interface DataTableProps {
  columns: DataTableColumn[];
  rows: Array<Record<string, ReactNode>>;
  /** The uppercase count on the header row: `ARTICLES (14)`. */
  caption?: string;
  className?: string;
}

export function DataTable({ columns, rows, caption, className }: DataTableProps) {
  return (
    <table className={['or-table', className].filter(Boolean).join(' ')}>
      {caption && <caption className="or-card__meta">{caption}</caption>}
      <thead>
        <tr>
          {columns.map((c) => (
            <th key={c.key} className={c.numeric ? 'or-table__num' : undefined}>{c.label}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((r, i) => (
          <tr key={i}>
            {columns.map((c) => (
              <td key={c.key} className={c.numeric ? 'or-table__num' : undefined}>{r[c.key]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
