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
  className?: string;
}

export function DataTable({ columns, rows, className }: DataTableProps) {
  return (
    <table className={['bl-table', className].filter(Boolean).join(' ')}>
      <thead>
        <tr>{columns.map((c) => (<th key={c.key} className={c.numeric ? 'bl-table__num' : undefined}>{c.label}</th>))}</tr>
      </thead>
      <tbody>
        {rows.map((r, i) => (
          <tr key={i}>{columns.map((c) => (<td key={c.key} className={c.numeric ? 'bl-table__num' : undefined}>{r[c.key]}</td>))}</tr>
        ))}
      </tbody>
    </table>
  );
}
